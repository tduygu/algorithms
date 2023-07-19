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

    def traverse(self):
        current = self.head
        # while current is not None:
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, target_index):
        current = self.head
        index = 0
        while current:
            if index == target_index:
                return current.value
            current = current.next
            index += 1
        return None

    def get2(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return True

    def set_value2(self, index, value):
        temp = self.get2(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp
        return None

    def pop_first(self):
        if self.head is None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.head is None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre_node = self.get2(self.length-2)
            pre_node.next = None
            self.tail = pre_node
        self.length -= 1
        return popped_node

    def pop2(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if self.length == 0 or index > self.length-1 or index < 0:
            return None
        if self.length == 1 and index == 0:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value
        elif index == self.length -1:
            return self.pop()
        else:
            pre_popped_node = self.get2(index-1)
            popped_node = pre_popped_node.next
            pre_popped_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        arr = []
        tempNode = self.head
        while tempNode:
            arr.append(tempNode.value)
            tempNode = tempNode.next
        arr.reverse()
        self.delete_all()
        for a in arr:
            self.append(a)

    def reverse2(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def findMiddle(self):
        if self.head is None:
            return None
        n = int(self.length / 2)
        up_to = n+1 if n % 2 == 0 else n
        ind = 0
        current_node = self.head
        for i in range(n):
            current_node = current_node.next
        return current_node

    def find_middle2(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node


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

new_empty_llist.traverse()

# print(new_empty_llist.search(46))
# print(new_empty_llist.search(20))
# print(new_empty_llist.get(2))
# print(new_empty_llist.get(5))
# print(new_empty_llist.get2(-1))
# print(new_empty_llist.get(1))
# new_empty_llist.set_value(2,1)
# print(new_empty_llist)
# new_empty_llist.set_value2(0,15)
# print(new_empty_llist)
# new_empty_llist.pop_first()
print(new_empty_llist)
linked_list2 = LinkedList()
linked_list2.traverse()
#print(linked_list2.pop_first())
# popped = new_empty_llist.pop()
# popped2 = linked_list2.pop()
#
# print(popped.value)
# print(f"{popped2.value if popped2 else None}")
# print(f"{linked_list2.head} - {linked_list2.tail} - {linked_list2.length}")
# linked_list2.prepend(5)
# linked_list2.traverse()
# print(f"{linked_list2.head.value} - {linked_list2.tail.value} - {linked_list2.length}")
# popped3 = linked_list2.pop()
# print(f"{popped3.value if popped3 else None} popped.")

print("************")
# print(new_empty_llist)
# removed = new_empty_llist.remove(3)
# print(removed.value)
# print(new_empty_llist)
# print(new_empty_llist.tail.value)

# linked_list3 = LinkedList()
# linked_list3.append(77)
# print(linked_list3)
# print(linked_list3.remove(0))
# print(linked_list3.remove(1))
# print(linked_list3.remove(-1))
# print(linked_list3.remove(5))

print("---------------")
# new_empty_llist.traverse()
# new_empty_llist.reverse2()
# new_empty_llist.traverse()

# middle = new_empty_llist.findMiddle()
# middle2 = new_empty_llist.find_middle2()
# print(middle.value)
# print(middle2.value)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(3)
ll.append(4)
ll.append(2)

ll.traverse()
ll.remove_duplicates()
print("-----")
ll.traverse()

