from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets, filters, status


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.BookSerializer
	queryset = models.Book.objects.all()