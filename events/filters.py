import django_filters
from .models import events

class FilterEvents(django_filters.FilterSet):
	topic = django_filters.CharFilter (lookup_expr = 'icontains')
	
	class Meta:
		fields = ['topic']


class FilterTests(django_filters.FilterSet):
	topic = django_filters.CharFilter (lookup_expr = 'icontains')
	
	class Meta:
		fields = ['topic']