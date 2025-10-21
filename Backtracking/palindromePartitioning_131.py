class Solution(object):
    def partition(self, s):
        res = []
        path = []

        def isPalindrome(st,ed):
            part = s[st:ed+1]
            return part == part[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start,len(s)):
                if isPalindrome(start,end):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()
            return

                
        backtrack(0)
        return res