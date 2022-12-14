from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Advertisement, Response


class AdvertisementFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Advertisement
       fields = {
           'heading': ['icontains'],
           'category': ['exact'],
           'author': ['exact']
       }


class ResponseFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Response
       fields = {
           'commentator': ['exact'],
           'advertisement': ['exact']
       }