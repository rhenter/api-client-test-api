import factory
import pytest

from ..utils import fake
from apps.book.models import Book

pytestmark = pytest.mark.django_db


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    name = factory.Sequence(lambda n: "Test Book %03d" % n)
    description = fake.text()
