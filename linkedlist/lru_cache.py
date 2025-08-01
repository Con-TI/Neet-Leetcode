# Doubly linked list

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0) # LRU and MRU dummy nodes, not modified but used as reference (like a -1 and n+1 node)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # Removes node from dll
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # Inserts node on MRU end
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update the order
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # return the value
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # Remove any existing node in dll
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Insert node to the end of dll
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # remove the lru
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
