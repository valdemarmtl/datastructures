from datastructures.linear_datastructures.linked_list.singly_linked_list import Node, SinglyLinkedList


class TestSinglyLinkedList:
    def test_node_init(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None

    def test_init(self):
        linked_list = SinglyLinkedList()
        assert linked_list.head is None

    def test_insert_at_beginning(self):
        linked_list = SinglyLinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)
        linked_list.prepend(3)
        assert linked_list.head.data == 3

    def test_insert_at_end(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        end_node = linked_list.get_node(2)
        assert end_node.data == 3
