from datastructures.linear_datastructures.sort.bubble_sort import bubble_sort


class TestBubbleSort:
    def test_bubble_sort(self):
        list_of_elements = [40, 30, 10, 50, 20]
        bubble_sort(list_of_elements)
        assert list_of_elements == [10, 20, 30, 40, 50]
