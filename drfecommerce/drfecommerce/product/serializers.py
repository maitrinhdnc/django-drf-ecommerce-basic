from rest_framework import serializers

from .models import *

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"