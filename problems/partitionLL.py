from linkedListProblems import LinkedList

def partition(ll, x):
    currNode = ll.head
    ll.tail = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < x:
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

customLinkedList = LinkedList()
customLinkedList.generate(10,0,10)
print(customLinkedList)
partition(customLinkedList, 8)
print(customLinkedList)




