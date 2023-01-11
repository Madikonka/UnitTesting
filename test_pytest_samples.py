import pytest_samples

def test_join_passed() -> None:
    # positive use case for many items
    assert pytest_samples.join([1,2,3], "-") == "1-2-3"


def test_join_one_passed() -> None:
    # positive use case for one item
    assert pytest_samples.join([0], "-") == "0"


def test_join_empty_passed() -> None:
    # positive use case for 0 items
    assert pytest_samples.join([], "-") == ""


def test_join_empty_passed() -> None:
    # positive use case for no denom
    assert pytest_samples.join([1,2,3], "") == "123"