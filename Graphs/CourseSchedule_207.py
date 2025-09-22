class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lst = [[]for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            [a,b] = prerequisites[i]
            lst[b].append(a)
        q=deque()
        indegree = [0]*numCourses
        for i in range(len(lst)):
            for v in lst[i]:
                indegree[v]+=1
        for i  in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for v in lst[curr]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        return len(ans)==numCourses


