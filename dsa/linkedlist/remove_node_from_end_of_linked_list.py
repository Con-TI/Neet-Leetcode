# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, head, n):
        if not head:
            return None
        head.next = self.rec(head.next,n)
        n[0] -= 1
        if n[0] == 0:
            return head.next
        return head
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute force (Store a nodes list and just reassign)
        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next
        
        # removeIndex = len(nodes)-n
        # if removeIndex == 0:
        #     return head.next
        # nodes[removeIndex-1].next = nodes[removeIndex].next
        # return head

        # Iteration (first pass to find length of list, 2nd pass to remove)
        # N = 0
        # cur = head
        # while cur:
        #     N+=1
        #     cur = cur.next
        # removeIndex = N-n

        # if removeIndex == 0:
        #     return head.next
        
        # cur = head
        # for i in range(N-1):
        #     if (i+1)==removeIndex:
        #         cur.next = cur.next.next
        #     cur = cur.next
        
        # return head
        
        # Recursion(Build recursion stack till end then 
        # use [n] as an index to keep track of, incrementing by 1)
        # return self.rec(head, [n])

        # Two pointers (One pass, right ptr starts shifted by n so that moving 
        # both ptrs simultaneously gets left to n-1)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
