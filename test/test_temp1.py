

import pytest


@pytest.fixture()
def create_user():
    created_user = 'Ivan'
    yield created_user
    created_user = ''
    print(created_user)

def test_1(create_user):
    print (create_user)

