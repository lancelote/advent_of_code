"""Global pytest fixtures."""
import pytest


@pytest.fixture
def mock_get_data(mocker):
    """aocd.get_data() call mock."""
    yield mocker.patch("main.get_data")
