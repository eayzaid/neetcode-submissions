class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i , j) :
            res = 0
            stack = deque()
            stack.append((i,j))
            while stack :
                i , j = stack.pop()
                if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                    continue
                if grid[i][j] != 1: 
                    continue
                res += 1
                grid[i][j] = -1
                stack.append((i+1,j))
                stack.append((i-1,j))
                stack.append((i,j-1))
                stack.append((i,j+1))
            return res
        ans = -1
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] != 1:
                    continue
                else :
                    ans = max(ans,dfs(i,j))
        return ans if ans > 0 else 0