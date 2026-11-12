from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {0 : []}
        for edge in edges : 
            adj.setdefault(edge[0],[]).append(edge[1])
            adj.setdefault(edge[1],[]).append(edge[0])
        stack = deque()
        seen = set()
        stack.append((0,-1))
        while stack :
            current_node , source = stack.pop()
            if current_node in seen : 
                return False
            seen.add(current_node)
            for neighbor in adj[current_node] :
                if neighbor == source : 
                    continue
                stack.append((neighbor,current_node))
        if len(seen) != n : 
            return False
        return True