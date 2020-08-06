from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'description',
            'is_active',
        ]

        read_only_fields = (
            'id',
        )
