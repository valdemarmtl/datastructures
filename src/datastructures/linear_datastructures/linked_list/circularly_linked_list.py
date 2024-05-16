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

    def delete_node(self, key: object):
        if self.head is None:
            return

        current_node = self.head
        prev_node = None
        while current_node.data != key:
            if current_node.next == self.head:
                return
            prev_node = current_node
            current_node = current_node.next
        if current_node == self.head:
            self._remove_head()
        else:
            prev_node.next = current_node.next
            self.size -= 1

    def delete_node_index(self, index: int):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        if self.head is None:
            return

        current_node = self.head
        prev_node = None
        count = 0
        while count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if current_node == self.head:
            self._remove_head()
        else:
            prev_node.next = current_node.next
            self.size -= 1

    def get_key(self, key: object, data_only: bool = False) -> Optional[Node] | object:
        current_node = self.head
        while current_node and current_node.data != key:
            if current_node.next == self.head:
                return None
            current_node = current_node.next
        if data_only and current_node:
            return current_node.data
        return current_node

    def get_index(self, index: int, data_only: bool = False) -> Node | object:
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")

        current_node = self.head
        count = 0
        while count != index:
            current_node = current_node.next
            count += 1
        if data_only and current_node:
            return current_node.data
        return current_node

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

    def _add_first_node(self, data: object):
        new_node = Node(data)
        self.head = new_node
        self.size += 1

    def _set_tail_next_to_new_head(self, new_head: Node):
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_head

    def _remove_head(self):
        if self.size == 1:
            self.head = None
        else:
            self._set_tail_next_to_new_head(self.head.next)
            self.head = self.head.next
        self.size -= 1


