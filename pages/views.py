import csv
import urllib

from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import TaskCreateForm
from .models import Task


class TaskCreateAndListView(ListView, ModelFormMixin):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form()
        task_todo = Task.objects.filter(status=0)
        task_doing = Task.objects.filter(status=1)
        task_done = Task.objects.filter(status=2)
        return render(request,
                      self.template_name,
                      {'todo': task_todo,
                       'doing': task_doing,
                       'done': task_done,
                       'form': self.form})

    def post(self, request, *args, **kwargs):
        print('TaskCreateAndListView.post start')

        self.object = None
        self.object_list = self.get_queryset()

        form = self.get_form()
        if form.is_valid():
            print('form_valid')
            return self.form_valid(form)
        else:
            print('form_invalid')
            return self.form_invalid(form)

    def form_valid(self, form):
        print('TaskCreateAndListView.form_valid start')
        task = form.save(commit=False)
        task.save()
        messages.success(self.request, f'タスク「{task.title}」を登録しました。')
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail_modal.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update_modal.html'
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        print('form_valid start')
        if self.request.is_ajax():
            print('request is Ajax')
            super().form_valid(form)
            # messages.success(self.request, '更新しました。')
            return render(self.request,
                          'task_detail_modal_body.html',
                          {'task': self.object})
        # messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form_invalid start')
        # messages.error(self.request, '更新に失敗しました。')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        print('post start')
        return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete_modal.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        print('delete start')
        messages.success(self.request, f'タスクを削除しました。')
        return super().delete(request, *args, **kwargs)


def export_task(request):
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    filename = urllib.parse.quote('tasks.csv')
    response['Content-Disposition'] = f'attachment; filename={filename}'

    header = ['ID', 'Title', 'Detail', 'Person in charge', 'Deadline', 'Status',
              'Create date', 'Update date']
    writer = csv.writer(response, lineterminator='\n')
    writer.writerow(header)
    for task in Task.objects.all():
        writer.writerow([task.pk,
                         task.title,
                         task.detail,
                         task.person_in_charge,
                         task.deadline_datetime,
                         task.get_status_display(),
                         task.create_datetime,
                         task.update_datetime])
    return response
