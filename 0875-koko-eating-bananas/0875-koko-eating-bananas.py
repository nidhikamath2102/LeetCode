import math
class Solution:
    def get_h(self, mid, piles):
        total_h=0
        for i in range(0,len(piles)):
            total_h+=math.ceil(piles[i]/mid)
        return total_h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max=0
        for i in range(0,len(piles)):
            if piles[i]>max: max=piles[i]

        l,r=1,max
        min=-1
        while l<=r:
            mid=(l+r)//2
            if self.get_h(mid,piles) <= h: 
                min=mid
                r=mid-1
            elif self.get_h(mid,piles) > h: l=mid+1
        return min