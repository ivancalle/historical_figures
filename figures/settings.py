"""Settings."""
import os
import pathlib
import random
import contextlib

__issuer__ = "figures"
__version__ = pathlib.Path('VERSION').read_text().strip()

MONGODB_DSN = os.environ.get('MONGODB_DSN', 'mongodb://localhost/figures')

# TEST SETTINGS
TEST_SEED = os.getenv('TEST_SEED', random.random())
with contextlib.suppress(Exception):  # Trying parse it to float
    TEST_SEED = float(TEST_SEED)

# LOGGING
LOG_FILE = os.getenv('LOG_FILE', f'/var/log/{__issuer__}.log')
LOG_FILE_MAX_BYTES = int(os.getenv('LOG_FILE_MAX_BYTES', 20000000))
LOG_FILE_NUMBER = int(os.getenv('LOG_FILE_NUMBER', 3))
