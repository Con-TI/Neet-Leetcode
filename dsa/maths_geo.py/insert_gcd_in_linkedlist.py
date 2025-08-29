class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Defined as inside function
        def gcd(a, b):
            while b>0:
                a, b = b, a%b
            return a
        
        cur = head
        while cur.next:
            temp = cur.next
            gcdval = gcd(cur.val, temp.val)
            gcdNode = ListNode(gcdval)
            cur.next = gcdNode
            gcdNode.next = temp
            cur = temp
        return head