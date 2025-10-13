class Solution(object):
    def floodFill(self, image, sr, sc, color):

        def dfs(mat, r, c, visited, color, val):
            visited[r][c] = True
            mat[r][c] = color
            for d in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr = r + d[0]
                nc = c + d[1]
                if isSafe(nr,nc,mat) and mat[nr][nc] == val and not visited[nr][nc]:
                    dfs(mat, nr, nc, visited, color, val)
            return 
        
        def isSafe(r, c, mat):
            return 0<=r<len(mat) and 0<=c<len(mat[0])

        m = len(image)
        n = len(image[0])
        val = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == sr and c == sc:
                    val = image[r][c]
                    dfs(image,r,c,visited,color,val)
        return image
        