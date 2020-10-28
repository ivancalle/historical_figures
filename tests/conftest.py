"""Global pytest config."""
from figures import settings


def pytest_report_header(config):
    """Adding info in report header."""
    return f"Test seed: {settings.TEST_SEED}"
