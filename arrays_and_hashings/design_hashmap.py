class Node:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.map = [Node() for i in range(10**3)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key,value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % len(self.map)
        cur = self.map[index].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next