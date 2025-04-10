class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr,s,i = [],sorted(nums),0
        while i<len(s):
            if s[i]>0:
                break
            if i>0 and s[i]==s[i-1]: 
                i+=1
                continue
            j,k=i+1,len(s)-1
            while j<k:
                total=s[i]+s[j]+s[k]
                if total==0: 
                    arr.append([s[i], s[j], s[k]])
                    while j<k and s[j]==s[j+1]:
                        j+=1
                    while j<k and s[k]==s[k-1]:
                        k-=1
                    k-=1
                    j+=1
                elif total>0: k-=1
                else: j+=1
            i+=1
        return arr