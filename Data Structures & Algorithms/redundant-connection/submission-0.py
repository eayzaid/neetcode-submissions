from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ## basically we start doing a dfs , it's guaranted that we're going to have one cycle
        ## we detect the edges that form the cycle , and then we search each of them to see who figure out last in the edges list
        n = len(edges)
        adj = {i : [] for i in range(1 , n + 1)}
        for idx , edge in enumerate(edges) : 
            adj[edge[0]].append((edge[1] , idx))
            adj[edge[1]].append((edge[0], idx))
        
        stack = deque()
        seen = set()
        source = [-1]* ( n + 1 ) 
        cycle_edges = []

        stack.append(1)

        while stack  :
            current_node = stack.pop()                
            seen.add(current_node)
            isCycle = False
            for neighbor_val in adj[current_node] :
                neighbor , idx =  neighbor_val[0] , neighbor_val[1]
                if neighbor == source[current_node] : ## we don't want to visit the node we came from
                    continue
                if neighbor in seen :
                    isCycle = True ## we detected a cycle
                    backward_pointer = current_node
                    ## we constrcut the edges that construct the cycle
                    cycle_edges.append([backward_pointer , neighbor])
                    while backward_pointer != neighbor : 
                        cycle_edges.append([backward_pointer,source[backward_pointer]])
                        backward_pointer = source[backward_pointer]
                    break 
                source[neighbor] = current_node
                stack.append(neighbor)
            if isCycle :
                break
        ans = []
        ans_idx = -1
        for edge in cycle_edges : 
            for neighbor in adj[edge[0]] : 
                if neighbor[0] == edge[1] and neighbor[1] > ans_idx : 
                    ans_idx = neighbor[1]
                    ans = edge
        return ans if ans in edges else [ans[1],ans[0]]
        
        


