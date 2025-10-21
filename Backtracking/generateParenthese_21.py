class Solution(object):
    def generateParenthesis(self, n):
        res = []
        stack = []
        op = [0]
        cp = [0]

        def backtrack():
            if len(stack) == (2*n):
                ans = "".join(stack)
                res.append(ans)
                return
            if op[0] < n:
                stack.append("(")
                op[0]+=1
                backtrack()
                stack.pop()
                op[0] -=1
            if cp[0] < op[0]:
                stack.append(")")
                cp[0]+=1
                backtrack()
                stack.pop()
                cp[0] -=1
            return
        
        backtrack()
        return res


        