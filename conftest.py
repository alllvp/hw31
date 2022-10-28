import pytest

from factories import SelectionFactory, UserFactory, AdFactory
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from pytest_factoryboy import register


register(SelectionFactory)
register(UserFactory)
register(AdFactory)


@pytest.fixture
def api_client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client
