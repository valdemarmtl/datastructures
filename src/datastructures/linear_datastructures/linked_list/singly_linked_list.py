from typing import Optional


class Node:
    def __init__(self, data: object):
        self.data: object = data
        self.next: Optional[Node] = None


class SinglyLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: object):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: object):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_node_at_pos(self, pos: int, data: object):
        if self.head is None or pos == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node and count != pos:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        prev_node.next = new_node
        new_node.next = current_node

    def delete_node(self, key: object):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos: int):
        if self.head:
            current_node = self.head
            if pos == 0:
                self.head = current_node.next
                current_node = None
                return
            count = 0
            while current_node and count != pos:
                prev_node = current_node
                current_node = current_node.next
                count += 1
            if current_node is None:
                return
            prev_node.next = current_node.next
            current_node = None
