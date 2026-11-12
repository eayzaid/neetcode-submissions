from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        n , m = len(grid) , len(grid[0])
        seen = set()
        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] == 2 : 
                    queue.append((i,j,0))
        ans = 0
        while queue :
            i , j , minutes_to_rotten = queue.popleft()

            if i < 0 or i >= n or j < 0 or j >= m : 
                continue
            if grid[i][j] == 0 : 
                continue

            if (i,j) in seen : 
                continue
            seen.add((i,j))

            grid[i][j] = 2
            ans = max(ans,minutes_to_rotten)
            queue.append((i+1,j,minutes_to_rotten + 1))
            queue.append((i-1,j,minutes_to_rotten + 1))
            queue.append((i,j+1,minutes_to_rotten + 1))
            queue.append((i,j-1,minutes_to_rotten + 1))

        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] == 1 : 
                    return -1
        
        return ans