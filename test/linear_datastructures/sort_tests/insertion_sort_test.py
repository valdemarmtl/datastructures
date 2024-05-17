import pytest
from datastructures.linear_datastructures.sort.insertion_sort import insertion_sort


class TestInsertionSort:

    @pytest.mark.parametrize("input, result", [
        ([3, 2, 1], [1, 2, 3]),
        ([40, 30, 10, 50, 20], [10, 20, 30, 40, 50]),
        ([5], [5]),
        ([], [])
    ])
    def test_insertion_sort(self, input, result):
        insertion_sort(input)
        assert input == result
