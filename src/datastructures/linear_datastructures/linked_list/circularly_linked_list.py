from typing import Optional


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next: Optional[Node] = None


class CircularlyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

    def append(self, data: object):
        if self.head is None:
            return self._add_first_node(data)

        new_node = Node(data)
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
        self.size += 1

    def prepend(self, data: object):
        if self.head is None:
            return self._add_first_node(data)

        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        self.head = new_node
        self.size += 1

    def insert_node_index(self, index: int, data: object):
        if index >= self.size:
            raise IndexError("Index out of range")
        if self.head is None or index == 0:
            return self.prepend(data)

        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node and count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        prev_node.next = new_node
        new_node.next = current_node
        self.size += 1

