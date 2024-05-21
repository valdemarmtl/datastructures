from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self) -> None:
        self.list_ = SinglyLinkedList()

    def enqueue(self, data: object) -> None:
        self.list_.append(data)

