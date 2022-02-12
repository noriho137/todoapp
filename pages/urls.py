from django.urls import path

from .views import (
    TaskCreateAndListView, TaskDetailView, TaskUpdateView, TaskDeleteView,
    export_task
)

urlpatterns = [
    path('', TaskCreateAndListView.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/export/', export_task, name='task_export'),
]
