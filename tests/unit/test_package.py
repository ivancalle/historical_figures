"""Package related tests."""


def test_import():
    """Test basic import."""
    import importlib
    try:
        importlib.import_module('figures')
    except ImportError:
        assert False
