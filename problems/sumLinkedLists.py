from linkedListProblems import LinkedList

def sumLists(ll1, ll2):
    if ll1.head is None or ll2.head is None:
        return None
    curr1 = ll1.head
    curr2 = ll2.head
    elde = 0

    ll3 = LinkedList()

    while curr1 or curr2:
        sum = elde
        # sum = curr1.value + curr2.value + elde
        if curr1:
            sum += curr1.value
            curr1 = curr1.next
        if curr2:
            sum += curr2.value
            curr2 = curr2.next

        nodeValue = sum % 10
        elde = sum // 10
        ll3.add(nodeValue)

    if elde != 0:
        ll3.add(elde)

    return ll3


def sumLists2(ll1, ll2):
    if ll1.head is None or ll2.head is None:
        return None
    curr1 = ll1.head
    curr2 = ll2.head
    carry = 0

    ll3 = LinkedList()
    while curr1 or curr2:
        result = carry
        if curr1:
            result += curr1.value
            curr1 = curr1.next
        if curr2:
            result += curr2.value
            curr2 = curr2.next
        ll3.add(int(result % 10))
        carry = result // 10

    if carry != 0:
        ll3.add(carry)

    return ll3


customLL1 = LinkedList()
customLL2 = LinkedList()

# customLL1.generate(3,1,9)
# customLL2.generate(4,1,9)
customLL1.add(6)
customLL1.add(3)
customLL1.add(7)

customLL2.add(8)
customLL2.add(8)
customLL2.add(4)
customLL2.add(9)

print(customLL1)
print(customLL2)
print(sumLists2(customLL1,customLL2))

