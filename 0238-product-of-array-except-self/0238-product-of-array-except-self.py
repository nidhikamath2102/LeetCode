class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m,zc,answer=1,0,[]

        for n in nums:
            if n!=0: m*=n
            else: zc+=1

        if zc>1: return [0]*len(nums)

        for n in nums:
            if zc==0: answer.append(m//n)
            elif zc==1 and n!=0: answer.append(0)
            elif zc==1 and n==0: answer.append(m)
        return answer