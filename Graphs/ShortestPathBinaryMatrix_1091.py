class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        dirt = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        def isSafe(r,c):
            return 0<=r<n and 0<=c<n
        q = deque()
        q.append((0,0,1))
        visited[0][0] = True
        while q:
            r,c, d,= q.popleft()
            if r==n-1 and c==n-1:
                return d
            for dr in dirt:
                nr = r+dr[0]
                nc = c+dr[1]
                if isSafe(nr,nc) and visited[nr][nc] == False and grid[nr][nc] == 0:
                    q.append((nr,nc,d+1))
                    visited[nr][nc] = True

        return -1