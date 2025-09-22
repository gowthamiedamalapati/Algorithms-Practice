class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        differenceArray = [0]* 1001
        for [p,f,t] in trips:
            differenceArray[f]+=p
            differenceArray[t]-=p
        if differenceArray[0]>capacity:
            return False
        for i in range(1,len(differenceArray)):
            differenceArray[i] = differenceArray[i]+differenceArray[i-1] 
            print(differenceArray[i])
            if differenceArray[i]>capacity:
                return False
        return True
        