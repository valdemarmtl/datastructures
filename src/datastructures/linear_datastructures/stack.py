
from datastructures.linear_datastructures.linked_list.singly_linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self.list_ = SinglyLinkedList()

    def push(self, data: object):
        self.list_.prepend(data)

