class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i<=j:
            n = numbers[i]+numbers[j]
            if n==target: return i+1,j+1
            elif n>target: j-=1
            else: i+=1