from collections import defaultdict

# Double ended linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = self.next    

class LRUCache:

    def __init__(self, capacity: int):
        # Needs a double linkedList and a HashMap
        self.cache = {}
        self.linkedList = list()
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
    
    # Insert at right
    def insert(self, node):
        pass

    def remove(self, node):
        pass
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, Node)
        if len(self.cache == self.capacity - 1):
            self.remove(self.end)
        self.insert(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)