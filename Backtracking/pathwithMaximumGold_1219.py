class Solution(object):
    def getMaximumGold(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = [0]
        pathSum = [0]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def isSafe(r,c):
            return 0<=r<m and 0<=c<n

        def backtrack(row,col):
            visited[row][col] = True
            pathSum[0]+=grid[row][col]
            res[0] = max(res[0],pathSum[0])
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr = row+d[0]
                nc = col+d[1]
                if isSafe(nr,nc) and grid[nr][nc] and not visited[nr][nc]:
                    backtrack(nr,nc)
            visited[row][col] = False
            pathSum[0]-=grid[row][col]
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    backtrack(i,j)
        return res[0]
