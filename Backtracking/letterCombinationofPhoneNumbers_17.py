class Solution(object):
    def letterCombinations(self, digits):
        res = []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }
        def backtrack(start,path):
            if start == len(digits):
                res.append(path)
                return

            letters = map[digits[start]]
            for l in letters:
                backtrack(start+1,path+l)
            return
        
        backtrack(0,"")
        return res
        
        
        