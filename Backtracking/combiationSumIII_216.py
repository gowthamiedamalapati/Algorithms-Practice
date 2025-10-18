class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        path = []

        def backtrack(start,sum):
            if sum == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(start,10):
                if sum+i > n:
                    break
                path.append(i)
                backtrack(i+1,sum+i)
                path.pop()
            return

        backtrack(1,0)
        return res
        