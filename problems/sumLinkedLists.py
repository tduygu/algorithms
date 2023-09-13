from linkedListProblems import LinkedList

def sumLists(ll1, ll2):
    if ll1.head is None or ll2.head is None:
        return None
    curr1 = ll1.head
    curr2 = ll2.head
    elde = 0

    ll3 = LinkedList()

    while curr1 and curr2:
        sum = curr1.value + curr2.value + elde
        nodeValue = sum % 10
        elde = sum // 10
        ll3.add(nodeValue)
        curr1 = curr1.next
        curr2 = curr2.next

    if elde != 0:
        ll3.add(elde)

    return ll3

customLL1 = LinkedList()
customLL2 = LinkedList()

customLL1.generate(3,1,9)
customLL2.generate(3,1,9)
print(customLL1)
print(customLL2)
print(sumLists(customLL1,customLL2))

