class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i,v in enumerate(nums):
            arr[v] = i
        
        for i,v in enumerate(nums):
            if target-v in arr and i!=arr[target-v]:
                return [i, arr[target-v]]