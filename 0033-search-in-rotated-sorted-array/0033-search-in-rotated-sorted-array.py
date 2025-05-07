class Solution:
    def binary_search(self, nums, l, r, target):
        while l<=r:
            mid=(l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid]<target:l=mid+1
            else:r=mid-1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        min=-1

        if nums[l]<=nums[r]: return self.binary_search(nums, l, r, target)

        while l<=r:
            mid=(l+r)//2
            if nums[mid-1]>=nums[mid]: 
                min=mid
                break
            elif nums[mid]>nums[r]: l=mid+1
            else: r=mid-1

        if (target<=nums[min] or target>=nums[min]) and target<=nums[len(nums)-1]:
            return self.binary_search(nums, min, len(nums)-1, target)
        else:
            return self.binary_search(nums, 0, min-1, target)
        