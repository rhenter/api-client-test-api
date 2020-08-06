from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        'id',
        'name',
        'is_active',
    ]
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
