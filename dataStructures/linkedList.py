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

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        temp_node = Node(value)
        if self.head is None:
            self.head = temp_node
            self.tail = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node
        self.length += 1

    def insert(self, value, index):
        if index < 0:
            return False
        if index >= self.length:
            self.append(value)
        elif self.length == 0 or index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            # n = 0
            # while n < index - 1:
            #     temp_node = temp_node.next
            #     n += 1
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
        return True







new_linked_list = LinkedList()
# print(new_linked_list)
print(new_linked_list.head)
print(new_linked_list.tail)
new_linked_list.append(50)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
new_linked_list.append(30)
new_linked_list.append(42)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.prepend(15)
print(new_linked_list)

new_empty_llist = LinkedList()
new_empty_llist.prepend(5)
print(new_empty_llist)

new_empty_llist.prepend(10)
new_empty_llist.append(46)
print(new_empty_llist)

new_empty_llist.insert(7,4)
print(new_empty_llist)
