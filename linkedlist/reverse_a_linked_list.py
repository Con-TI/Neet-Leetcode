# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteration
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        """
        E.g. [1,2,3,4]
        
        iter 1
        curr = 1 -> 2 -> 3 -> 4
        temp = 2 -> 3 -> 4
        curr = 1 -> None
        prev = 1 -> None
        curr = 2 -> 3 -> 4

        iter 2
        curr = 2 -> 3 -> 4
        temp = 3 -> 4
        curr = 2 -> 1 -> None
        prev = 2 -> 1 -> None
        curr = 3 -> 4

        ...
        """

        # Recursion
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

        """
        E.g. [1,2,3,4]
        Stack building + Unwinding (Makes use of addresses, ptrs and objects in Python)
        
        rec(1):
            head = 1 -> 2 -> 3 -> 4
            newHead = 1 -> 2 -> 3 -> 4
            rec(2):
                head = 2 -> 3 -> 4
                newHead = 2 -> 3 -> 4
                rec(3):
                    head = 3 -> 4
                    newHead = 3 -> 4
                    rec(4):
                        head = 4
                        newHead = 4
                        head = 4 -> None
                        return newHead   # base case hit

                    # back to rec(3)
                    newHead = 4
                    (Python objects are references in memory, leading to a cycle)
                    head.next.next = head  →  4.next = 3 
                    (This next step breaks the cycle)
                    head.next = None       →  3.next = None
                    (newHead becomes 4->3 from the .next.next assignment)
                    return newHead (4 -> 3)

                # back to rec(2)
                newHead = 4 -> 3
                (Currently head = 2 -> 3)
                head.next.next = head  →  3.next = 2
                head.next = None       →  2.next = None
                return newHead (4 -> 3 -> 2)

            # back to rec(1)
            newHead = 4 -> 3 -> 2
            head = 1
            head.next = 2
            head.next.next = head  →  2.next = 1
            head.next = None       →  1.next = None
            return newHead (4 -> 3 -> 2 -> 1)
        """