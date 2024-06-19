#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Solution
        # anagram_map = defaultdict(list)
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagram_map[sorted_word].append(word)
        
        # return list(anagram_map.values())

        dict_list = [] #[dict_0,dict_1]
        ans = [] #[["bat"],["nat","tan"]]

        for str in strs:
            new_dict = defaultdict(int)
            
            # get dict
            for s in str:
                new_dict[s] += 1

            found_match = False
            for i, dict in enumerate(dict_list):
                # find match
                if dict == new_dict:
                    ans[i].append(str)
                    found_match = True
                    break

            # no match
            if not found_match:
                dict_list.append(new_dict)
                ans.append([str])

        return ans
# @lc code=end

