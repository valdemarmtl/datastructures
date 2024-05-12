from datastructures.linear_datastructures.linked_list.doubly_linked_list import DoublyLinkedList, Node


class TestDoublyLinkedList:
    def test_node_init(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None
        assert node.prev is None

    def test_init(self):
        linked_list = DoublyLinkedList()
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_insert_at_beginning(self):
        linked_list = DoublyLinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)
        linked_list.prepend(3)
        assert linked_list.head.data == 3

    def test_insert_at_end(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        assert linked_list.tail.data == 3

