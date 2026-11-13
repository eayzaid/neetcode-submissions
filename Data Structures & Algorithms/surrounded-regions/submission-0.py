class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        def dfs(i,j,replace_with) : 
            stack = deque()
            stack.append((i,j))
            while stack  :
                i , j = stack.pop()
                if i >= n or i < 0 or j >= m or j < 0 : 
                    continue
                if (i,j) in seen : 
                    continue
                if board[i][j] != 'O' : 
                    continue
                seen.add((i,j))
                board[i][j] = replace_with
                stack.append((i+1,j))
                stack.append((i-1,j))
                stack.append((i,j+1))
                stack.append((i,j-1))
            
        n , m = len(board) , len(board[0])

        for i in range(n) : 
            if board[i][0] == 'O' :
                dfs(i,0,"N") 
            if board[i][m-1] == 'O' : 
                dfs(i,m-1,"N")
        
        for i in range(m) : 
            if board[0][i] == 'O' :
                dfs(0,i,"N") 
            if board[n-1][i] == 'O' : 
                dfs(n-1,i,"N")
        
        for i in range(n) : 
            for j in range(m) :
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'
        