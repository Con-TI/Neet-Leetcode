# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iteration
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry
            carry = val // 10
            val = val%10 
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

        # Own solution
        num1 = 0
        i = 0
        while l1:
            num1 += l1.val*(10**i)
            l1 = l1.next
            i += 1
        
        num2 = 0
        i = 0
        while l2:
            num2 += l2.val*(10**i)
            l2 = l2.next
            i += 1

        res = num1 + num2

        node = ListNode(res%10)
        return_node = node
        while res != 0.0:
            res -= res%10
            res /= 10
            if res != 0:
                node.next = ListNode(int(res)%10)
            node = node.next

        return return_node