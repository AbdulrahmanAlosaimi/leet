import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertGreatestCommonDivisors(head):
    ptr = head
    while (ptr.next):
        ptr.next = ListNode(math.gcd(ptr.val, ptr.next.val), ptr.next)
        ptr = ptr.next.next

    return head


l1 = ListNode(18)
l1.next = ListNode(6)
l1.next.next = ListNode(10)
l1.next.next.next = ListNode(3)

print(insertGreatestCommonDivisors(l1).next.next.next.val)
