#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        emailToAcc = {} #email -> acc
        # 初步將有重複的email集合起來
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    # union acc index
                    uf.union(i,emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        print(uf.parents) 
        # acc 對應的 parent acc -> [0, 0, 2, 3]
        print(emailToAcc)
        # {'johnsmith@mail.com': 0, 'john_newyork@mail.com': 0, 'john00@mail.com': 1, 'mary@mail.com': 2, 'johnnybravo@mail.com': 3}

        emailGroup = defaultdict(list) #index of acc -> list of emails
        
        #產生 acc index 對應的 mail
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)

        print(emailGroup)
        #  {0: ['johnsmith@mail.com', 'john_newyork@mail.com', 'john00@mail.com'], 2: ['mary@mail.com'], 3: ['johnnybravo@mail.com']})
        
        res = []
        for i,emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res
# @lc code=end

