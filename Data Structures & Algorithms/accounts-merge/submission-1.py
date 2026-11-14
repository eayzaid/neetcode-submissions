class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = {}
        for account in accounts : 
            number_of_emails = len(account) - 1
            pivot = account[1]
            adj[pivot] = [] if pivot not in adj else adj[pivot]
            for idx_email in range(1,number_of_emails) :
                adj[pivot].append(account[1 + idx_email])
                adj.setdefault(account[1 + idx_email],[]).append(pivot)
        seen = set()
        ans = []
        for account in accounts : 
            if account[1] in seen : 
                continue
            stack = deque([account[1]])
            user_account = []
            while stack  :
                email = stack.pop()
                if email in seen :
                    continue
                seen.add(email)
                user_account.append(email)
                for other_emails in adj[email]:
                    stack.append(other_emails)
            user_account.sort()
            user_account = [account[0]] + user_account
            ans.append(user_account)
        return ans
