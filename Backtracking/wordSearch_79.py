class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]


        def backtrack(index,r,c):
            if index == len(word):
                return True
            if ((r<0 or r >= m) or (c<0 or c>=n) or
               (visited[r][c]) or (board[r][c] != word[index])):
                return False
            visited[r][c] = True
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr = d[0] + r
                nc = d[1] + c
                if backtrack(index+1, nr, nc):
                    return True
            visited[r][c] = False
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(0,i,j):
                    
                    return True
        return False
        