class Solution(object):
    def countComponents(self, n, edges):

        def dfs(graph, u, seen):
            seen.add(u)
            for v in graph[u]:
                if v not in seen:
                    dfs(graph, v, seen)
            return
            
        graph = [[]for _ in range(n)]
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(graph, i, seen)
        return count 