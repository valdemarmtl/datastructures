from typing import Optional


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next: Optional[Node] = None


class CircularlyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

