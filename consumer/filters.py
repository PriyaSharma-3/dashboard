import django_filters
# from .filters import ConsumerFilter
from .models import Consumer

class ConsumerFilter(django_filters.FilterSet):
    class Meta:
        model = Consumer
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields =['FeederName','Date_Time','Username']
