#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # [A,A,A,B,B,C] n = 2
        # 至少需 A _ _ A _ _ A   3*2+1
        # [A,A,A,B,B,B,C] n = 2
        # 至少需 A B _ A B _ A B 3*2+2

        ele_count = {}
        for ele in tasks:
            if ele not in ele_count:
                ele_count[ele] = 1
            else:
                ele_count[ele] += 1
        
        max_num = 0 #出現頻率最多是多少
        max_count = 0 #出現頻率最高的元素有幾個

        for ele,num in ele_count.items():
            if max_num < num:
                max_num = num
                max_count = 1
            elif max_num == num:
                max_count += 1

        intervals = (max_num-1)*(n+1)+max_count

        return max(len(tasks),intervals)


# @lc code=end

