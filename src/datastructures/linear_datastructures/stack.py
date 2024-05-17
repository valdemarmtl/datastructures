from typing import Optional

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

    def peek(self) -> Optional[object]:
        return self.list_.head.data if self.list_.head else None

    def get(self, index: int) -> Optional[object]:
        return self.list_.get_index(index, data_only=True)

    def is_empty(self) -> bool:
        return self.list_.head is None

    def __len__(self) -> int:
        return self.list_.len_iterative()
