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

    def prepend(self, data: object):
        if self.head is None:
            self._add_first_node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_node_index(self, index: int, data: object):
        if self.head is None or index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node and count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if prev_node is self.tail:
            self.append(data)
        else:
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current_node
            current_node.prev = new_node

    def delete_node(self, key: object):
        current_node = self.head
        if current_node and current_node.data == key:
            if not current_node.next:
                self._reset_list()
            else:
                self._delete_head()
            current_node = None
            return
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        if current_node is self.tail:
            self._delete_tail()
        else:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node
        current_node = None

    def delete_node_index(self, index: int):
        current_node = self.head
        if current_node and index == 0:
            if not current_node.next:
                self._reset_list()
            else:
                self._delete_head()
            current_node = None
            return
        count = 0
        while current_node and count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        if current_node is self.tail:
            self._delete_tail()
        else:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node
        current_node = None

    def get_key(self, key: object, data_only: bool = False) -> Optional[Node] | object:
        current_node = self.head
        while current_node and current_node.data != key:
            current_node = current_node.next
        if data_only and current_node:
            return current_node.data
        return current_node

    def get_index(self, index: int, data_only: bool = False) -> Optional[Node] | object:
        current_node = self.head
        count = 0
        while current_node and count != index:
            current_node = current_node.next
            count += 1
        if data_only and current_node:
            return current_node.data
        return current_node

    def len_iterative(self) -> int:
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def _reset_list(self):
        self.head = None
        self.tail = None

    def _delete_head(self):
        self.head = self.head.next
        self.head.prev = None

    def _delete_tail(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def _add_first_node(self, data: object):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    linked_list.prepend(0)
    linked_list.print_list()
    linked_list.insert_node_index(1, 4)
    linked_list.print_list()
    linked_list.delete_node(2)
    linked_list.print_list()
    linked_list.delete_node_index(0)
    linked_list.print_list()
    linked_list.delete_node(3)
    linked_list.print_list()
    linked_list.delete_node(1)
    linked_list.print_list()
    linked_list.delete_node(0)
    linked_list.print_list()
    linked_list.delete_node(1)
