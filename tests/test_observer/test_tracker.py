import io
import logging
import sys

import pytest

from llmnet.observer.tracker import track


@pytest.fixture
def captured_output():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    yield captured_output
    sys.stdout = sys.__stdout__


def test_log_debug_level(captured_output):
    handler = logging.StreamHandler(captured_output)
    track.addHandler(handler)
    x = 1
    track.warning(f"Test: {x}")
    output = captured_output.getvalue().strip()
    assert "Test: 1" in output


def test_log_level(captured_output):
    handler = logging.StreamHandler(captured_output)
    track.addHandler(handler)
    track.setLevel(logging.WARNING)
    assert track.level == logging.WARNING
