"""Conftest."""
import pytest
import random
import mimesis

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.testclient import TestClient
from figures.app import factory
from figures import settings


random.seed(settings.TEST_SEED)


@pytest.fixture(scope='session')
def app():
    """Return a configured app instance."""
    app = factory()
    app.state.client_db = AsyncIOMotorClient("mongodb://localhost/test")
    app.state.db = app.state.client_db.get_database()
    yield app
    app.state.client_db.drop_database("test")
    app.state.client_db.close()


@pytest.fixture(scope='session')
def client(app):
    """Return a configured test client instance."""
    return TestClient(app)


def _create_figure():
    """Create a fake figure."""
    person = mimesis.Person(seed=random.random())
    dt = mimesis.Datetime(seed=random.random())
    text = mimesis.Text(seed=random.random())

    figure = {
        'name': person.full_name(),
        'description': text.text(),
        'birthdate': dt.formatted_datetime(fmt='%Y-%m-%d',
                                               end=2002),
        'date_death': None if random.random() < 0.5 else dt.formatted_datetime(
            fmt='%Y-%m-%d', start=2002, end=2020),
        'tags': [text.word() for i in range(0, random.randint(0, 10))]
    }

    return figure


def create_update_figure():
    """Create a update for figure."""
    return {k: v for k, v in _create_figure().items() if v is not None and random.random() < 0.5}  # noqa E501


@pytest.fixture(scope='session')
def figures():
    """Return a list of figures."""
    return [_create_figure() for i in range(0, random.randint(2, 10))]
