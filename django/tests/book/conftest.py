import pytest

from tests.utils import fake


@pytest.fixture
def book_data():
    return {
        'name': 'Livro Teste',
        'description': fake.text()
    }
