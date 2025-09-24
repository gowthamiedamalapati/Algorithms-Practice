class Solution(object):
    def shipWithinDays(self, weights, days):
        l = max(weights)
        h = sum(weights)
        ans = -1
        while l <= h:
            m = (l+h)//2
            if self.isfeasible(m,weights, days):
                ans = m
                h = m-1
            else:
                l=m+1
        return ans
    def isfeasible(self,md,weights, days):
         count = 0
         cap = 0
         for w in weights:
            if w+cap<=md:
                cap+=w
            else:
                count+=1
                cap = w
         return count+1<=days
