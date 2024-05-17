
from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self.list_ = SinglyLinkedList()

    def push(self, data: object):
        self.list_.prepend(data)

    def pop(self, index: int = 0) -> object:
        if self.is_empty():
            raise ValueError("Stack is empty")
        data = self.list_.get_index(index, data_only=True)
        self.list_.delete_node_index(index)
        return data

