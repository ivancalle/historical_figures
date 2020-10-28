"""Figures handlers."""
from . import figures


def setup(app):
    """Add routes."""
    app.include_router(figures.router, prefix="/api/v1/figures")
