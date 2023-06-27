class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# new_node = Node(10)
# print(new_node)

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


new_linked_list = LinkedList()
# print(new_linked_list)
print(new_linked_list.head)
print(new_linked_list.tail)
new_linked_list.append(50)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
new_linked_list.append(30)
print(new_linked_list.length)
