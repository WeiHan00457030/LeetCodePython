#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        seen = {} # record last seen character
        ans,leftIndex = 0,0;

        for rightIndex in range(len(s)) :
            print(rightIndex,s[i])

            # never seen -> add in to dict, compare max length
            if s[rightIndex] not in seen:
                seen[s[rightIndex]] = rightIndex
                ans = max(ans,rightIndex-leftIndex+1)
                print('ans=',ans)
            # seen before
            else :
                # last seen index < leftIndex -> not in the current word
                # add in to dict, compare max length
                if seen[s[rightIndex]] < leftIndex:
                    ans = max(ans,rightIndex-leftIndex+1)
                    seen[s[rightIndex]] = rightIndex
                # last seen index > leftIndex -> character in the current word
                # move left index to last seen index+1, update last seen index
                else:
                    leftIndex = seen[s[rightIndex]] +1
                    seen[s[rightIndex]] = rightIndex
        return ans
# @lc code=end

