from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        def dfs(i , j) : 
            stack = deque()
            stack.append((i,j))
            while stack : 
                i , j = stack.pop()
                if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                    continue
                if grid[i][j] != '1': 
                    continue
                grid[i][j] = '-1'
                stack.append((i+1,j))
                stack.append((i-1,j))
                stack.append((i,j-1))
                stack.append((i,j+1))
        ans = 0
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] != '1':
                    continue
                else : 
                    ans += 1
                    dfs(i,j)
        return ans