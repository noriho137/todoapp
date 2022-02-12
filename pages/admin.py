from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail', 'status', 'person_in_charge',
                    'deadline_datetime', 'create_datetime', 'update_datetime')


admin.site.register(Task, TaskAdmin)
