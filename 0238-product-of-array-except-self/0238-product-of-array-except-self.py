class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf,answer=[1],[1],[]
        for i in range(1, len(nums)):
            pre.append(pre[-1]*nums[i-1])

        for i in range(len(nums)-2,-1,-1):
            suf.insert(0,suf[0]*nums[i+1])
    

        for i in range(len(pre)):
            answer.append(pre[i]*suf[i])
        return answer