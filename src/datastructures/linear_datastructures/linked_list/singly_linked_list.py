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

    def get(self, pos: int) -> Optional[object]:
        current_node = self.head
        count = 0
        while current_node and count != pos:
            current_node = current_node.next
            count += 1
        return current_node.data if current_node else None
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
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.print_list()
    linked_list.prepend("E")
    linked_list.print_list()
    linked_list.insert_node_at_pos(1, "F")
    linked_list.print_list()
    linked_list.delete_node("B")
    linked_list.print_list()
    linked_list.delete_node_at_pos(2)
    linked_list.print_list()
    print(linked_list.len_iterative())
    print(linked_list.len_recursive(linked_list.head))
