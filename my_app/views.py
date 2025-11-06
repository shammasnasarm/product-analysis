from django.db import models
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter

# Create your views here.


class ProductViewSet(viewsets.ViewSet, GenericAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    @action(detail=False, methods=["get"], url_path="analytics")
    def analytics(self, request):
        """
        API endpoint to get analytics data for products based on filters.
        Requests can filter by category and price range.
        """
        cache_key = "product_analytics"
        cached_data = cache.get(cache_key) # Check cache first
        if cached_data:
            # If cached data exists, return it
            return Response(cached_data)
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.annotate(
            total_value=models.F("price") * models.F("stock")
        ).aggregate(
            total_products=models.Count("id"),
            avg_price=models.Avg("price"),
            total_stock_value=models.Sum("total_value")
        )

        serializer = self.serializer_class(queryset)
        cache.set(cache_key, serializer.data) # Cache the result
        return Response(serializer.data)
