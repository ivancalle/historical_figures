"""Logger."""
import logging


class LoggerAdapter(logging.LoggerAdapter):
    """Adapt logger."""

    def process(self, msg, kwargs):
        """Process log."""
        extra = self.extra.copy()

        if 'extra' in kwargs:
            extra.update(kwargs.pop('extra'))

        kwargs['extra'] = extra

        params = kwargs.pop('params', {})
        extra['params'] = ' '.join(f'{key}={params[key]};' for key in params)

        return msg, kwargs


def getLogger(name, extra=None):
    """Return context adapt logger."""
    logger = logging.getLogger(name)
    return LoggerAdapter(logger, extra or {})
