class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, value):
        node = Node(value)

        if self.head is None:
            self.head = self.tail = node
            self.size += 1
        else:
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
            self.size += 1

    def insert_tail(self, value):
        node = Node(value)

        if self.tail is None:
            self.head = self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def front(self):
        return self.head.val

    def back(self):
        return self.tail.val

    def print_linked_list(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next


my_linked_list = DoublyLinkedList()

my_linked_list.insert_head("A")
my_linked_list.insert_head("B")
my_linked_list.insert_tail("C")
my_linked_list.insert_tail("D")
my_linked_list.insert_tail("E")
my_linked_list.insert_tail("F")

my_linked_list.remove("F")
my_linked_list.remove_last()

my_linked_list.print_linked_list()
print(f"size of this doubly linked list: {my_linked_list.size}")
