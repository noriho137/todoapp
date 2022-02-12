import django.forms.fields
from django.forms import ModelForm

from .models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'detail', 'status', 'person_in_charge',
                  'deadline_datetime',)
        labels = {'title': 'タイトル',
                  'detail': '詳細',
                  'status': 'ステータス',
                  'person_in_charge': '担当者',
                  'deadline_datetime': '期限'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if type(field) is django.forms.fields.DateTimeField:
                field.input_formats = ['%Y-%m-%d %H:%M:%S']
                field.widget.attrs['class'] = 'form-control datetimepicker-input'
                field.widget.attrs['data-target'] = '#datetimepicker1'
            else:
                field.widget.attrs['class'] = 'form-control'
