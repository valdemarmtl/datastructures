from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self) -> None:
        self.list_ = SinglyLinkedList()

    def enqueue(self, data: object) -> None:
        self.list_.append(data)

    def dequeue(self) -> object:
        if self.is_empty():
            raise ValueError("Queue is empty")
        data = self.list_.get_index(0, data_only=True)
        self.list_.delete_node_index(0)
        return data

    def peek(self) -> object:
        return self.list_.head.data if self.list_.head else None

