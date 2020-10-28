"""Database hooks."""
from motor.motor_asyncio import AsyncIOMotorClient

from ... import settings


def start_create(app):
    """Start database."""
    def start():
        app.state.client_db = AsyncIOMotorClient(settings.MONGODB_DSN)
        app.state.db = app.state.client_db.get_database()

    return start


def finish_create(app):
    def finish():
        """Close database."""
        app.state.client_db.close()

    return finish
