from typing import Optional


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, data: object):
        if self.tail is None:
            self._add_first_node(data)
            return
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def _add_first_node(self, data: object):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node

