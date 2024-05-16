from datastructures.linear_datastructures.linked_list.circularly_linked_list import CircularlyLinkedList, Node


class TestCircularlyLinkedList:
    def test_node_init(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None

    def test_circularly_linked_list_init(self):
        circular_linked_list = CircularlyLinkedList()
        assert circular_linked_list.head is None
        assert circular_linked_list.size == 0

    def test_append(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next == circular_linked_list.head
        assert circular_linked_list.size == 1

        circular_linked_list.append(2)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next.data == 2
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_prepend(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.prepend(1)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next == circular_linked_list.head
        assert circular_linked_list.size == 1

        circular_linked_list.prepend(2)
        assert circular_linked_list.head.data == 2
        assert circular_linked_list.head.next.data == 1
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_insert_node_index(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(3)
        circular_linked_list.insert_node_index(1, 2)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next.data == 2
        assert circular_linked_list.head.next.next.data == 3
        assert circular_linked_list.head.next.next.next == circular_linked_list.head
        assert circular_linked_list.size == 3

