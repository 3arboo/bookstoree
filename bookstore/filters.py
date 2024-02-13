import django_filters
from .models import Order

class OrderFilters(django_filters.FilterSet):
    class  Meta:
        model = Order
        fields = {'book','stauts'}
    