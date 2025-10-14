class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        def dfs(u):
            visited[u] = True
            if u == destination:
                return True
            for v in graph[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
            return False
        
        graph = [[] for _ in range(n)]
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False for _ in range(n)]
        print(graph)
        return dfs(source)
        