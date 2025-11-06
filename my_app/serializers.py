from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    """
    Serializer for Product analytics data.
    Fields:
    - total_products: Total number of products
    - avg_price: Average price of products
    - total_stock_value: Total stock value of all products
    """
    total_products = serializers.IntegerField()
    avg_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_stock_value = serializers.DecimalField(max_digits=15, decimal_places=2)
