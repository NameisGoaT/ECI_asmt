# views.py
from django_filters import OrderingFilter
from rest_framework import viewsets, pagination
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        'book_id': ['in', 'exact'],
        'language': ['in', 'exact'],
        'mime_type': ['in', 'exact'],
        'subjects': ['in', 'exact', 'icontains'],
        'bookshelves': ['in', 'exact', 'icontains'],
        'author': ['in', 'exact', 'icontains'],
        'title': ['in', 'exact', 'icontains'],
    }
    search_fields = ['book_id', 'language', 'mime_type', 'subjects', 'bookshelves', 'author', 'title']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-popularity')
