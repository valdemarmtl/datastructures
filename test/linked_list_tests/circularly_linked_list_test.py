import pytest

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

    def test_delete_node(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        circular_linked_list.append(3)
        circular_linked_list.delete_node(2)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next.data == 3
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_delete_node__head(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        circular_linked_list.append(3)
        circular_linked_list.delete_node(1)
        assert circular_linked_list.head.data == 2
        assert circular_linked_list.head.next.data == 3
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_delete_node__single_node(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.delete_node(1)
        assert circular_linked_list.head is None
        assert circular_linked_list.size == 0

    def test_delete_node__empty_list(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.delete_node(1)
        assert circular_linked_list.head is None
        assert circular_linked_list.size == 0

    def test_delete_node__not_found(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.delete_node(2)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next == circular_linked_list.head
        assert circular_linked_list.size == 1

    def test_delete_node_index(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        circular_linked_list.append(3)
        circular_linked_list.delete_node_index(1)
        assert circular_linked_list.head.data == 1
        assert circular_linked_list.head.next.data == 3
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_delete_node_index__head(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        circular_linked_list.append(3)
        circular_linked_list.delete_node_index(0)
        assert circular_linked_list.head.data == 2
        assert circular_linked_list.head.next.data == 3
        assert circular_linked_list.head.next.next == circular_linked_list.head
        assert circular_linked_list.size == 2

    def test_delete_node_index__single_node(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.delete_node_index(0)
        assert circular_linked_list.head is None
        assert circular_linked_list.size == 0

    def test_delete_node_index__empty_list(self):
        circular_linked_list = CircularlyLinkedList()
        with pytest.raises(IndexError):
            circular_linked_list.delete_node_index(1)

    def test_delete_node_index__out_of_range(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        with pytest.raises(IndexError):
            circular_linked_list.delete_node_index(1)

    def test_delete_node_index__negative_index(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        with pytest.raises(IndexError):
            circular_linked_list.delete_node_index(-1)

    def test_get_key(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        node = circular_linked_list.get_key(2)
        assert node.data == 2

    def test_get_key__data_only(self):
        circular_linked_list = CircularlyLinkedList()
        circular_linked_list.append(1)
        circular_linked_list.append(2)
        data = circular_linked_list.get_key(2, data_only=True)
        assert data == 2

