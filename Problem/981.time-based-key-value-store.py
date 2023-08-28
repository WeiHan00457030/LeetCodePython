#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.cur_dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.cur_dict:
            self.cur_dict[key]=[""]
        self.cur_dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.cur_dict:
            return ""
        
        for i in self.cur_dict[key][::-1]:
            print(i)
            if i and i[1] <= timestamp:
                return i[0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

