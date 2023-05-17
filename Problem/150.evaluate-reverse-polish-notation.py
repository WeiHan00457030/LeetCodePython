#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        operators = ['+','-','*','/']
        for i in tokens:
            if i not in operators:
                num.append(i)
            else:
                b = int(num.pop())
                a = int(num.pop())
                match i:
                    case '+':
                        tmp = a+b
                        num.append(tmp)
                    case '-':
                        tmp = a-b
                        num.append(tmp)
                    case '*':
                        tmp = a*b
                        num.append(tmp)
                    case '/':
                        tmp = a/b
                        num.append(tmp)

        return int(num[0])
# @lc code=end

