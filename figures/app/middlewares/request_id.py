"""Request id middleware."""
import uuid

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from ...settings import __issuer__
from ...settings import __version__


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """Request id middleware."""
        request_id = request.headers.get('X-Request-ID')

        if not request_id:
            request_id = str(uuid.uuid4())

        request.state.id = request_id

        try:
            response = await call_next(request)
            response.headers['X-Request-ID'] = request_id
            response.headers['X-Issuer-Name'] = __issuer__
            response.headers['X-Issuer-Version'] = __version__
            return response

        except HTTPException as exception:
            exception.headers['X-Request-ID'] = request_id
            exception.headers['X-Issuer-Name'] = __issuer__
            exception.headers['X-Issuer-Version'] = __version__
            raise exception
