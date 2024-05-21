import pytest

from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList
from datastructures.linear_datastructures.queue import Queue


class TestQueue:
    def test_init(self):
        queue = Queue()

        assert queue.list_.head is None
        assert isinstance(queue.list_, SinglyLinkedList)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)

        assert queue.list_.head.data == 1

        queue.enqueue(2)

        assert queue.list_.head.next.data == 2

