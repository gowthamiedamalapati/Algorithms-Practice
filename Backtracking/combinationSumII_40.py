class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort() 
        res = []
        path = []

        def backtrack(start, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if target < candidates[i]:
                    break
                path.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                path.pop()

        backtrack(0,target)
        return res