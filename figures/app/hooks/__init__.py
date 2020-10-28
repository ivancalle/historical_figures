"""Application hooks."""
from . import database


def setup(app):
    """Add hooks."""
    app.add_event_handler("startup", database.start_create(app))
    app.add_event_handler("shutdown", database.finish_create(app))
