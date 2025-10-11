class Solution(object):
    def numIslands(self, grid):

        def dfs(grid, r, c, visited, dr):
            visited[r][c] = True
            for d in dr:
                nr = r+d[0]
                nc = c+d[1]
                if isSafe(nr,nc,grid) and not visited[nr][nc] and grid[nr][nc] == "1":
                    dfs(grid, nr, nc, visited, dr)
            return


        def isSafe(r,c,grid):
            return 0<=r<len(grid) and 0<=c<len(grid[0])


        m = len(grid)
        n = len(grid[0])
        dr = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and  grid[r][c] == "1":
                    dfs(grid, r, c, visited, dr)
                    count+=1
        return count
