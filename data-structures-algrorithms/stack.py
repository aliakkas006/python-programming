from linked_list import DoublyLinkedList


# stack implementation:

class Stack:
    def __init__(self):
        self.__linked_list = DoublyLinkedList()

    def push(self, value):
        self.__linked_list.insert_tail(value)

    def pop(self):
        val = self.__linked_list.back()
        self.__linked_list.remove_last()
        return val

    def is_empty(self):
        return self.__linked_list.size == 0

    def peek(self):
        return self.__linked_list.back()

    def __len__(self):
        return self.__linked_list.size


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

# print("Peak value of this stack:", my_stack.peek())
# print("Remove from this stack:", my_stack.pop())
# print("Length of my stack:", len(my_stack))
# print("Is my stack is empty:", my_stack.is_empty())
