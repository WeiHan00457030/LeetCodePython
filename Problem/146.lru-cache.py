#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

#TODO : rewrite after 5/21

# 使用dict 以在O(1)內找到元素, dict裡存的是一個雙向linked list的node
# 使用雙向linked list已在O(1)刪除元素, 如果是單向的話需要知道prev是誰,雙向則可以直接取得prev跟next
class LinkedNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.__evict(key)
        self.__addToEnd(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.__delete(key)

        node = LinkedNode(key, value)
        self.cache[key] = node
        self.__addToEnd(node)

        if len(self.cache) > self.capacity:
            self.__delete(self.head.next.key)
    
    def __evict(self, key) -> LinkedNode: 
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def __delete(self, key) -> None:
        deleteNode = self.__evict(key)
        del deleteNode
        del self.cache[key]

    def __addToEnd(self, node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

