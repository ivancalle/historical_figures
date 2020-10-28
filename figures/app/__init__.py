"""Figures app."""
from fastapi import FastAPI

from . import middlewares
from . import handlers
from . import hooks
from .. import settings


def factory():
    """Build app."""
    app = FastAPI(version=settings.__version__,
                  title=settings.__issuer__,
                  description="Historical figures API")

    hooks.setup(app)
    middlewares.setup(app)
    handlers.setup(app)

    return app


app = factory()
