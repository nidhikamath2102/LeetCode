class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rep={}
        for i,n in enumerate(nums):
            cmp = target-n
            if cmp in rep:
                return [rep[cmp],i]
            rep[n]=i