class Solution(object):
    def islandPerimeter(self, grid):

        def dfs(grid, r, c, visited, count):
            visited[r][c] = True
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr = r + d[0]
                nc = c + d[1]
                if not isSafe(nr,nc,grid) or grid[nr][nc] == 0:
                    count[0]+=1
                elif not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(grid, nr, nc, visited, count)
            return
              
        def isSafe(r,c,grid):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = [0]
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == 1:
                    dfs(grid, r ,c, visited, count)

        return count[0]
        