from django.shortcuts import render

from .models import Book, Person, User
from rest_framework import viewsets, filters
from .serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
