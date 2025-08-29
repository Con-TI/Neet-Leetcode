"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Recursion and hashmap
        # if head is None:
        #     return None
        # if head in self.map:
        #     return self.map[head]
        
        # copy = Node(head.val)
        # self.map[head] = copy
        # copy.next = self.copyRandomList(head.next)
        # copy.random = self.map.get(head.random)
        # return copy

        # Hash map (two pass)
        # n = 0
        # oldToCopy = {}
        # tmp = head
        # while tmp and tmp not in oldToCopy:
        #     node = Node(tmp.val)
        #     oldToCopy[tmp] = node
        #     tmp = tmp.next
        #     n += 1
        
        # i = 0
        # tmp = head
        # while tmp and i != n:
        #     node = oldToCopy[tmp]
        #     node.next = oldToCopy.get(tmp.next)
        #     node.random = oldToCopy.get(tmp.random)
        #     tmp = tmp.next
        #     i += 1

        # return oldToCopy.get(head)

        # Hash map (one pass by instantiating empty nodes for all)
        # oldToCopy = collections.defaultdict(lambda:Node(0))
        # oldToCopy[None] = None

        # cur = head
        # while cur:
        #     oldToCopy[cur].val = cur.val
        #     oldToCopy[cur].next = oldToCopy[cur.next]
        #     oldToCopy[cur].random = oldToCopy[cur.random]
        #     cur = cur.next
        
        # return oldToCopy[head]

        # Space Optimized I (Constant extra space excluding the copy)
        ## Builds l1 -> l2 -> l1.next -> l2.next -> l1.next.next ... zig zag pointers
        if head is None:
            return None
        
        l1 = head
        while l1 is not None:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        

        ## newHead = l2
        newHead = head.next

        ## Points the random pointers for each of the l2 nodes
        l1 = head
        while l1 is not None:
            if l1.random is not None:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        ## Fixes the pointer arrangement
        l1 = head
        while l1 is not None:
            l2 = l1.next
            l1.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
