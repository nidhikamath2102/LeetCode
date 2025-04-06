class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr,s,i = [],sorted(nums),0
        while i<len(s):
            if i>0 and s[i]==s[i-1]: 
                i+=1
                continue
            j,k=i+1,len(s)-1
            while j<k:
                sum=s[i]+s[j]+s[k]
                if sum==0: 
                    arr.append([s[i], s[j], s[k]])
                    while j<k and s[j]==s[j+1]:
                        j+=1
                    while j<k and s[k]==s[k-1]:
                        k-=1
                    k-=1
                    j+=1
                elif sum>0: k-=1
                else: j+=1
            i+=1
        return arr