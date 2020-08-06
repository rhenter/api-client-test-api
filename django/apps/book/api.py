from apps.core.viewsets import BaseViewSet
from .models import Book
from .serializers import BookSerializer


class BookViewSet(BaseViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_fields = (
        'is_active',
    )
    search_fields = (
        'name',
    )
