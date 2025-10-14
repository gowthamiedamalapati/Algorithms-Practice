class Solution(object):
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        path = []
        res = []
        def dfs(s):
            if s == n-1:
                res.append(path[:])
            for v in graph[s]:
                path.append(v)
                dfs(v)
                path.pop()
            return
        
        path.append(0)
        dfs(0)
        return res
