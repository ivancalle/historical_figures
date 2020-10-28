"""Application middlewares."""
from . import logger
from . import request_id


def setup(app):
    """Add middlewares."""
    app.add_middleware(logger.LoggerMiddleware)
    app.add_middleware(request_id.RequestIDMiddleware)
