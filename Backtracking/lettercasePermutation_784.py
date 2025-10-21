class Solution(object):
    def letterCasePermutation(self, s):
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path)
                return
            i=start
            if s[i].isnumeric():
                backtrack(i+1,path+s[i])
            else:
                backtrack(i+1,path+s[i].lower())
                backtrack(i+1,path+s[i].upper())
            # return
        backtrack(0,"")
        return res
        