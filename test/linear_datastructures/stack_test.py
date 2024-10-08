from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList
from datastructures.linear_datastructures.stack import Stack


class TestStack:
    def test_init(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert len(stack) == 0
        assert isinstance(stack.list_, SinglyLinkedList)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3
        assert stack.get(0) == 3
        assert stack.get(1) == 2
        assert stack.get(2) == 1

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert len(stack) == 0

    def test_pop_index(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop(1) == 2
        assert stack.pop(0) == 3
        assert stack.pop(0) == 1
        assert len(stack) == 0

    def test_pop_empty(self):
        stack = Stack()
        try:
            stack.pop()
        except ValueError as e:
            assert str(e) == "Stack is empty"

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.peek() == 3
        stack.pop()
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1
        stack.pop()
        assert stack.peek() is None

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False
        stack.pop()
        assert stack.is_empty() is True

    def test_len(self):
        stack = Stack()
        assert len(stack) == 0
        stack.push(1)
        assert len(stack) == 1
        stack.push(2)
        assert len(stack) == 2
        stack.pop()
        assert len(stack) == 1
        stack.pop()
        assert len(stack) == 0
