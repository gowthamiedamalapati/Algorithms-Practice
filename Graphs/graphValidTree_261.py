class Solution(object):
    def validTree(self, n, edges):

        def cycleCheck(graph,u,visited,parent, seen):
            visited[u] = True
            seen.add(u)
            for v in graph[u]:
                if  not visited[v]:
                    cycleCheck(graph,v,visited,u,seen)
                elif v!=parent:
                    return False
            return True

        graph = [[]for _ in range(n)]
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        seen = set()
        
        return cycleCheck(graph,0,visited,-1,seen) and len(seen) == n
        

# For agraph to be valid tree, graph should not have cycle and graph is  not disconnected connected(more than one componet)