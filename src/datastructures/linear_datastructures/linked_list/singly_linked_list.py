from typing import Optional


class Node:
    def __init__(self, data: object):
        self.data: object = data
        self.next: Optional[Node] = None


class SinglyLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
