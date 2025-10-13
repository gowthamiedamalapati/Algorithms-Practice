class Solution(object):
    def solve(self, board):

        def dfs(r,c,board,visited):
            visited[r][c] = True
            board[r][c] = "G"
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr = r+d[0]
                nc = c+d[1]
                if isSafe(nr,nc, board) and not visited[nr][nc] and board[nr][nc] == "O":
                    dfs(nr,nc,board,visited)
            return

        def isSafe(r,c,board):
            return 0<=r<len(board) and 0<=c<len(board[0])

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if board[0][i] == "O":
                dfs(0,i,board,visited)
        for i in range(1,m):
            if board[i][n-1] == "O":
                dfs(i,n-1,board,visited)
        for i in range(n-2,-1,-1):
            if board[m-1][i] == "O":
                dfs(m-1,i,board,visited)
        for i in range(m-2,0,-1):
            if board[i][0] == "O":
                dfs(i,0,board,visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "G":
                    board[i][j] = "O"
                
        return board
        