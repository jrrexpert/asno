from rest_framework import serializers
from .models import Product, Category

class ProductAddSerializer (serializers.Serializer):
    name = serializers.CharField()
    logo = serializers.ImageField(required=False)
    description = serializers.CharField()
    price = serializers.FloatField()
    size = serializers.CharField()
    category_id = serializers.IntegerField()


    def validate_category_id(self, data):
        category_id = data
        if not Category.objects.filter(id=category_id).exists():
            raise serializers.ValidationError("There is not such a record")
        return data

    def save(self):
        product = Product()
        product.name = self.validated_data['name']
        product.description = self.validated_data['description']
        product.size = self.validated_data['size']
        product.price = self.validated_data['price']
        product.logo = self.validated_data['logo']
        product.category_id = self.validated_data['category_id']
        product.save()
