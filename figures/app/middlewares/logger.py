"""Logger middleware."""
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from ... import logging

logger = logging.getLogger(__name__)


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """Logger middleware."""
        logger.info(
            'Request received',
            params={
                'method': request.method,
                'url': request.url,
                'ip': request.headers.get('X-Real-IP', request.client),
                'user_agent': request.headers.get('User-Agent'),
                'accept': request.headers.get('Accept'),
                'content_type': request.headers.get('Content-Type'),
            },
            extra={"id": request.state.id})

        try:
            response = await call_next(request)
            logger.info(
                'Response sent',
                params={
                    'status': response.status_code,
                    'content_type': response.headers.get('Content-Type')
                },
                extra={"id": request.state.id})
            return response

        except HTTPException as exception:
            logger.info(
                'Response sent',
                params={
                    'status': exception.status_code,
                    'content_type': exception.headers.get('Content-Type')
                })
            raise exception
