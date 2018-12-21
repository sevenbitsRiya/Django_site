import django_filters
from .models import Category, Product
class PriceFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['price']