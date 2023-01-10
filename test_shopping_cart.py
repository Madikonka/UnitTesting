import pytest

def test_passed():
    assert True


def test_failed(example_fixture):
    assert False