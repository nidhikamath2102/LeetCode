class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c,answer=1,[1]
        for i in range(1, len(nums)):
            answer.append(answer[-1]*nums[i-1])

        for i in range(len(nums)-2,-1,-1):
            c*=nums[i+1]
            answer[i]*=c

        return answer