from datastructures.linear_datastructures.linked_list.singly_linked_list import Node, SinglyLinkedList


class TestSinglyLinkedList:
    def test_node_init(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None

    def test_init(self):
        linked_list = SinglyLinkedList()
        assert linked_list.head is None
