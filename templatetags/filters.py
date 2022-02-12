import datetime

from django import template


register = template.Library()


@register.filter
def remaining_days(deadline_datetime):
    if deadline_datetime is None:
        remaining = datetime.timedelta(days=999)
    else:
        deadline_date = deadline_datetime.date()
        today = datetime.datetime.today().date()
        remaining = deadline_date - today
    return remaining.days
