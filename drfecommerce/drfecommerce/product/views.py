from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from .models import Category
from .serializers import CategorySerailizer

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerailizer(self.queryset, many=True)
        return Response(serializer.data)

