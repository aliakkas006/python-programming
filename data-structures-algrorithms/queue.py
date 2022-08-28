from linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.__linked_list = DoublyLinkedList()

    def enqueue(self, value):
        self.__linked_list.insert_tail(value)

    def dequeue(self):
        val = self.__linked_list.front()
        self.__linked_list.remove_first()
        return val

    def front(self):
        return self.__linked_list.front()

    def is_empty(self):
        return self.__linked_list.size == 0

    def __len__(self):
        return self.__linked_list.size

# my_queue = Queue()
#
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(4)
# my_queue.enqueue(5)
#
# print("Remove from this queue:", my_queue.dequeue())
# print("Front value:", my_queue.front())
# print(f"length of my queue: {len(my_queue)}")
# print("Is my queue is empty:" ,my_queue.is_empty())
