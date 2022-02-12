from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    detail = models.TextField(max_length=1024, blank=True, null=True)
    person_in_charge = models.CharField(max_length=128, blank=True, null=True)
    deadline_datetime = models.DateTimeField(blank=True, null=True)
    status = models.PositiveIntegerField(choices=((0, 'ToDo'),
                                                  (1, 'Doing'),
                                                  (2, 'Done')),
                                         blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
