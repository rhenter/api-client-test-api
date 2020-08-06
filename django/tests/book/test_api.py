import json

import pytest
from django.urls import reverse
from rest_framework import status
from unipath import Path

from apps.book.models import Book
from .factories import BookFactory

pytestmark = pytest.mark.django_db

BASE_DIR = Path(__file__).ancestor(4)


@pytest.mark.parametrize('value,', [5, 10, 2, 40])
def test_book_api_list(value, admin_client):
    BookFactory.create_batch(value)

    url = reverse('api-book:books-list')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['count'] == value
    assert Book.objects.count() == value


def test_book_api_detail(admin_client, book):
    url = reverse('api-book:books-detail', args=[book.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['code'] == book.code


def test_book_api_post(admin_client, book_data):
    url = reverse('api-book:books-list')

    response = admin_client.post(url, data=json.dumps(book_data), content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.filter(name=book_data['name']).exists()


def test_book_api_patch(admin_client, book):
    data = {"name": "Book Name"}
    url = reverse('api-book:books-detail', args=[book.code])
    response = admin_client.patch(url, data=json.dumps(data), content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['name'] == data['name']
    assert Book.objects.filter(name=data['name']).exists()


def test_book_api_put(admin_client, book):
    data = book.serialize()
    data['name'] = 'Book Name'
    data.pop('parent')
    url = reverse('api-book:books-detail', args=[book.code])
    response = admin_client.put(url, data=json.dumps(data), content_type="application/json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['name'] == data['name']
    assert Book.objects.filter(name=data['name']).exists()
