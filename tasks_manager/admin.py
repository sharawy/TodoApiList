from django.contrib import admin

# Register your models here.
from tasks_manager.models import TodoTask


@admin.register(TodoTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','start_date','remind_me_at')
    exclude = ('celery_task_id',)