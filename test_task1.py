import pytest

from task1 import array_diff

def test_array_diff_with_single_match():
    assert array_diff([1, 2], [1]) == [2]

def test_array_diff_with_multiple_matches():
    assert array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]

def test_array_diff_with_no_matches():
    assert array_diff([1, 2, 3], [4, 5, 6]) == [1, 2, 3]

def test_array_diff_with_empty_second_list():
    assert array_diff([1, 2, 3], []) == [1, 2, 3]

def test_array_diff_with_empty_first_list():
    assert array_diff([], [1, 2, 3]) == []

def test_array_diff_with_identical_lists():
    assert array_diff([1, 2, 3], [1, 2, 3]) == []