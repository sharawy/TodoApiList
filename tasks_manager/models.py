from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from tasks_manager.tasks import send_reminder
from TodoList.celery import app


class TodoTask(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    remind_me_at = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    celery_task_id = models.TextField(blank=True,null=True)

    def clean(self):
        super(TodoTask, self).clean()
        if self.remind_me_at :
            if self.remind_me_at > self.start_date:
                raise ValidationError("Reminder time must be before the task time")
            if self.remind_me_at <= timezone.now():
                raise ValidationError("Can't define previous time as reminder")

    def save_reminder_task(self):

        # remove task if it exist for updating reminder time
        #  not working with local settings
        app.control.revoke(self.celery_task_id)
        celery_task_id = send_reminder.apply_async((self,),eta=self.remind_me_at)
        self.celery_task_id = celery_task_id

    def save(self, *args, **kwargs):
        self.save_reminder_task()
        super(TodoTask, self).save(*args, **kwargs)

