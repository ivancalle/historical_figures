#!/usr/bin/env python
"""Figures entrypoint."""
import argparse
import logging
import uvicorn

from logging.handlers import RotatingFileHandler

from . import settings
from .settings import __version__

parser = argparse.ArgumentParser(prog='figures')
parser.add_argument('--version', action='version', version=__version__)
parser.add_argument('--debug', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--reload', action='store_true')
parser.add_argument('--workers', type=int, default=1)

cmd = parser.add_subparsers(dest='cmd')

serve_cmd = cmd.add_parser('serve', help='Run server')
serve_cmd.add_argument('--port', type=int, default=8000)

args = parser.parse_args()

logger = logging.getLogger('figures')
logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

fmt = f'$asctime|$levelname|{__version__}|$name|$id|$message|$params'
logfmt = logging.Formatter(fmt, style='$')

if not args.debug:
    _handler = RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=settings.LOG_FILE_MAX_BYTES,
        backupCount=settings.LOG_FILE_NUMBER)
    _handler.setFormatter(logfmt)
    _handler.setLevel(logging.INFO)
    logger.addHandler(_handler)

if args.verbose:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logfmt)
    _handler.setLevel(logging.DEBUG)
    logger.addHandler(_handler)

if args.cmd == 'serve':
    uvicorn.run("figures.app:app", host="0.0.0.0",
                port=args.port, reload=args.reload, workers=args.workers)

else:
    parser.print_help()
    exit(1)
