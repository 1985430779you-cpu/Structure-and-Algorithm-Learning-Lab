class Solution:
    def accountsMerge(self, accounts):
        from collections import defaultdict

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"]]
print(Solution().accountsMerge(accounts))    