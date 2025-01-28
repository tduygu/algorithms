class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            pre_last_node = self.tail
            pre_last_node.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of range")
            return
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            self.length += 1
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.length:
                self.append(value)
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next
                new_node.next = temp_node.next
                temp_node.next = new_node
                self.length += 1


test_list_1 = CSLinkedList()
# test_list_1.append(5)
# test_list_1.append(10)
# test_list_1.append(15)
# test_list_1.prepend(0)
# print(test_list_1)
# test_list_1.insert(4,20)
# # test_list_1.insert(1,3)
# print(test_list_1)
# print(test_list_1.length)
test_list_1.insert(0,-5)
test_list_1.insert(0,-10)
print(test_list_1)
print(test_list_1.length)
test_list_1.insert(9,99)
print(test_list_1)


