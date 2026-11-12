class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n)}
        for edge in edges : 
            adj.setdefault(edge[0],[]).append(edge[1])
            adj.setdefault(edge[1],[]).append(edge[0])
        stack = deque()
        seen = set()
        ans = 0
        for i in range(n) :
            if i not in seen :  
                stack.append(i)
                ans += 1
            while stack :
                current_node = stack.pop()
                if current_node in seen : 
                    continue
                seen.add(current_node)
                for neighbor in adj[current_node] :
                    stack.append(neighbor)
        return ans