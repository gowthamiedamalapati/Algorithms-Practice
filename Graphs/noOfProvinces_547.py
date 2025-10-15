class Solution(object):
    def findCircleNum(self, isConnected):
        graph = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        def dfs(u):
            seen[u]= True
            for v in graph[u]:
                if not seen[v]:
                    dfs(v)
            return 

        count = 0
        seen = [False for _  in range(len(graph))]
        for i in range(len(graph)):
            if not seen[i]:
                count+=1
                dfs(i)
        return count
        


#creating graph is not required we can use the given isConnected list to traverse
