# 双指针链表，链表里存储key和val,然后用一个哈希表存储key到节点的映射

class doublelist_dict:
    def __init__(self, key, val, nxt=None, pre=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.pre = pre

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = doublelist_dict(-1, -1)
        self.tail = doublelist_dict(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def add2head(self, key, val):
        node = doublelist_dict(key, val)
        self.dict[key] = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def move2head(self, key):
        node = self.dict[key]
        node.next.pre = node.pre
        node.pre.next = node.next
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def dellast(self):
        node = self.tail.pre
        self.tail.pre = node.pre
        node.pre.next =self.tail
        del self.dict[node.key]

    def get(self, key: int) -> int:
        if key in self.dict:
            self.move2head(key)
            return self.dict[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            self.move2head(key)
        else:
            if len(self.dict) == self.capacity:
                self.dellast()
            self.add2head(key, value)
