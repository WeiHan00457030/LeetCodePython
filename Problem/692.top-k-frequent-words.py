#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
import collections,heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        
        heap = [(-count,word) for word,count in counts.items()]

        heapq.heapify(heap)

        l = heapq.nsmallest(k,heap)
        
        return [word[1] for word in l]
        
        
# @lc code=end

