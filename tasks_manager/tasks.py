from celery import  task
from django.core.mail import EmailMessage

from TodoList.settings import CELERY_RETRY_TIME


@task(default_retry_delay=CELERY_RETRY_TIME)
def send_reminder(todo_task):
    try:
        subject = "Reminder Mail"
        body = "This a reminder mail for your task : "+todo_task.name+" at:"+str(todo_task.start_date)
        email = EmailMessage(subject, body, to=[todo_task.owner.email])
        print("send email return:"+str(email.send()))
    except Exception as e:
        send_reminder.retry(exc=e)