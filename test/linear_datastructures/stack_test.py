from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList
from datastructures.linear_datastructures.stack import Stack


class TestStack:
    def test_init(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert len(stack) == 0
        assert isinstance(stack.list_, SinglyLinkedList)

