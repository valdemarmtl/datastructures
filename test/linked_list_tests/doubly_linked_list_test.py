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

    def test_insert_node_index(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.insert_node_index(1, 4)
        node = linked_list.get_index(1)
        assert node.data == 4

    def test_delete_node(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.delete_node(2)
        node = linked_list.get_index(1)
        assert node.data == 3
        linked_list.delete_node(1)
        assert linked_list.head.data == 3
        assert linked_list.tail.data == 3
        linked_list.delete_node(3)
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_node__empty(self):
        linked_list = DoublyLinkedList()
        linked_list.delete_node(1)
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_node_index(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.delete_node_index(1)
        node = linked_list.get_index(1)
        assert node.data == 3
        linked_list.delete_node_index(0)
        assert linked_list.head.data == 3
        assert linked_list.tail.data == 3
        linked_list.delete_node_index(0)
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_delete_node_index__empty(self):
        linked_list = DoublyLinkedList()
        linked_list.delete_node_index(1)
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_get_key(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        node = linked_list.get_key(2)
        assert node.data == 2
        assert isinstance(node, Node)

    def test_get_key__empty(self):
        linked_list = DoublyLinkedList()
        assert linked_list.get_key(1) is None

    def test_get_key__data_only(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        data = linked_list.get_key(2, data_only=True)
        assert data == 2
        assert isinstance(data, object)

    def test_get_index(self):
        linked_list = DoublyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        node = linked_list.get_index(1)
        assert node.data == 2
        assert isinstance(node, Node)

