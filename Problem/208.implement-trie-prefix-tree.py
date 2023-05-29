#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['end'] = True

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur:
                return False
            else:
                cur = cur[letter]
        
        if 'end' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter in cur:
                cur = cur[letter]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

