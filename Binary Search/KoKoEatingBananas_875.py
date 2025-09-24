import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        lo = 1
        hg = max(piles)
        ans = -1
        while lo <= hg:
           md = (lo+hg)//2
           if self.isfeasible(md,piles,h):
               ans = md
               hg = md-1
           else:
                lo=md+1
        return ans

    def isfeasible(self,md,piles,h):
        k = 0
        for i in range(len(piles)):
            k+=ceil(piles[i]/float(md))
        return k<=h

