class UnionFind(object):
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)] 
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        u_rep =self.find(u)
        v_rep =self.find(v)
        if self.rank[u_rep] < self.rank[v_rep]:
            self.parent[u_rep] = v_rep
        elif self.rank[u_rep] > self.rank[v_rep]:
            self.parent[v_rep] = u_rep
        else:
            self.parent[v_rep] = u_rep
            self.rank[u_rep]+=1
        return 

class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFind(n)
        for [a,b] in edges:
            if uf.find(a) == uf.find(b):
                return[a,b]
            else:
                uf.union(a,b)
        return
