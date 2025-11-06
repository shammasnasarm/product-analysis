import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    """
    Filter class for Product model to filter by category and price range.
    """
    category = django_filters.CharFilter(
        field_name='category',
        lookup_expr='iexact'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lt'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gt'
    )

    class Meta:
        model = Product
        fields = ['category']
