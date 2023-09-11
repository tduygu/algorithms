from linkedListProblems import LinkedList

def remove_duplicates1(ll):
    arr = set()
    currNode = ll.head

    while currNode and currNode.next:
        arr.add(currNode.value)
        if currNode.next.value in arr:
            currNode.next = currNode.next.next
            currNode.next.next.prev = currNode
            currNode = currNode.next.next
        if currNode.prev and currNode.prev == currNode:
            currNode.prev.next = currNode.next
            currNode.next = currNode.prev
        else:
            currNode=currNode.next


def remove_duplicates(ll):
    if ll.head is None:
        return

    current_node = ll.head
    prev_node = None

    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current_node
        current_node = current_node.next

    ll.tail = prev_node
    return ll.head

abc = LinkedList()
abc.add(1)
abc.add(2)
abc.add(2)
abc.add(3)
abc.add(4)
abc.add(4)
abc.add(4)
abc.add(5)
print(abc)
print(remove_duplicates(abc))
print(abc)

