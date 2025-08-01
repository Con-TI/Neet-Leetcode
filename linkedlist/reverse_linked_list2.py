# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        priorleft = None
        if left > 1:
            i = left-2
            priorleft = head
            while i:
                priorleft = priorleft.next
                i-=1
        leftNode = head
        rightNode = head
        n = right-left+1
        left -= 1
        right -= 1


        while left or right:
            if left:
                prev = leftNode
                leftNode = leftNode.next
                left -= 1
            if right:
                rightNode = rightNode.next
                right -= 1

        # Reverse
        prev = rightNode.next
        curr = leftNode
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n-=1
        
        if priorleft is not None:
            priorleft.next = rightNode
            return head

        return rightNode

        """
        e.g.
        [1,2,3,4,5]
        curr = 1
        prev = 4
        temp = 2
        1 -> 4
        prev = 1
        curr = 2
        temp = 3
        2 -> 1 -> 4
        prev = 2
        curr = 3
        temp = 4
        3 -> 2 -> 1 -> 4
        """
