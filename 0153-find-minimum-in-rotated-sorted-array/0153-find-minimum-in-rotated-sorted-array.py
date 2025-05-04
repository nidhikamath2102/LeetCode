class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid-1]>nums[mid] and mid<len(nums)-1 and nums[mid]<nums[mid+1]: return nums[mid]
            elif nums[l]<=nums[r]: return nums[l]
            elif nums[mid]>nums[r]: l=mid+1
            else: r=mid-1