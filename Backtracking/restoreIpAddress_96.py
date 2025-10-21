class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        
        def valid(p):
            if p[0]=="0" and len(p)>1:
                return False
            elif not p.isnumeric():
                return False
            elif  int(p) > 255:
                return False
            return True

        def backtrack(start,path,k):
            if k == 0 and start == len(s) :
                res.append(path)
                return
            if k == 0 or start == len(s):
                return
            for i in range(start, len(s)):
                part = s[start:i+1]
                if len(part)<=3 and valid(part):
                    next_path = part if not path else (path + "." + part)
                    backtrack(i+1,next_path,k-1)
            return
        
        backtrack(0,"",4)
        return res
        