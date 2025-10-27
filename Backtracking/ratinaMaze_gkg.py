class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        res = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        def isSafe(r,c):
            return 0<=r<n and 0<=c<n
        
        def backtrack(row, col,path):
            if row == n-1 and col == n-1:
                res.append(path)
                return
            # visited[row][col] = True
            for d in [[0,1,"R"],[1,0,"D"],[0,-1,"L"],[-1,0,"U"]]:
                nr = row+d[0]
                nc = col+d[1]
                if isSafe(nr,nc) and maze[nr][nc] and not visited[nr][nc]:
                      visited[nr][nc] = True
                      backtrack(nr,nc,path+d[2])
                      visited[nr][nc] = False
            
        visited[0][0] = True
        backtrack(0,0,"")
        if len(res)>=2:
            res.sort()
        return res
        