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

