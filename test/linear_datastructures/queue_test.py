import pytest

from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList
from datastructures.linear_datastructures.queue import Queue


class TestQueue:
    def test_init(self):
        queue = Queue()

        assert queue.list_.head is None
        assert isinstance(queue.list_, SinglyLinkedList)
