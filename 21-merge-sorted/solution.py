class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Pointer to manipulate ListNodes
    ptr = ListNode()
    
    # Edge cases
    if list1 == None and list2 == None: return ListNode('')
    if list1 == None: return list2
    if list2 == None: return list1

    # First pointer
    if (list1.val < list2.val):
        ptr = ListNode(list1.val)
        list1 = list1.next
    else:
        ptr = ListNode(list2.val)
        list2 = list2.next
    
    # Head variable used for returning
    head = ptr
    
    
    while (list1 != None or list2 != None):
        
        # List1 is done, rest is list2 since its sorted
        if list1 == None:
            ptr.next = list2
            break

        # List2 is done, rest is list1 since its sorted
        elif list2 == None:
            ptr.next = list1
            break

        # Pointer at list2 is larger than list1 pointer
        elif list1.val < list2.val:
            ptr.next = ListNode(list1.val)
            ptr = ptr.next
            list1 = list1.next
            
        # Pointer at list1 is larger than list2 pointer
        elif list1.val > list2.val:
            ptr.next = ListNode(list2.val)
            ptr = ptr.next
            list2 = list2.next

        # Pointers are equal
        else:
            ptr.next = ListNode(list2.val)
            ptr = ptr.next
            list2 = list2.next
            
            ptr.next = ListNode(list1.val)
            ptr = ptr.next
            list1 = list1.next
    return head

first = ListNode(5)

second = ListNode(1)
second.next = ListNode(2)
second.next.next = ListNode(4)


result = mergeTwoLists(first, second)
while (result != None):
    print(result.val)
    result = result.next
