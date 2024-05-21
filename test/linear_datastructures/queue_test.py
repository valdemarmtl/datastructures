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

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        assert queue.dequeue() == 1
        assert queue.list_.head.data == 2

    def test_dequeue__empty(self):
        queue = Queue()
        with pytest.raises(ValueError) as e:
            queue.dequeue()

            assert str(e) == "Queue is empty"

    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)

        assert queue.peek() == 1

        queue.enqueue(2)

        assert queue.peek() == 1

    def test_peek__empty(self):
        queue = Queue()

        assert queue.peek() is None

