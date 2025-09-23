class Solution(object):
    def findClosestElements(self, arr, k, x):
        low = 0
        high = len(arr)
        while low<high:
            mid=(low+high)//2
            if arr[mid] <= x:
                low = mid+1
            else:
                high = mid
        
        i = low - 1 
        j = low
        print(low)
        r=0
        while( i>-1 or j<len(arr)) and r<k:
        
            iDiff = abs(arr[i]-x) if i>=0 else float("inf")
            jDiff = abs(arr[j]-x) if j<len(arr) else float("inf")
            if iDiff <= jDiff:
                i-=1
            else:
                j+=1
            r+=1
        return arr[i+1:j]