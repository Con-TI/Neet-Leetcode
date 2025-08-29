class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        # self.set = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % len(self.set) 
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

        # if self.contains(key):
        #     pass
        # else:
        #     self.set.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % len(self.set) 
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        # if self.contains(key):
        #     self.set.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = key % len(self.set) 
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        # if key in self.set:
        #     return True
        # return False

