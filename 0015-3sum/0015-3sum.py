class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i,s,arr=0,sorted(nums),[]
        while i<len(s)-2:
            while i>0 and i<len(s)-2 and s[i]==s[i-1]: 
                i+=1
                continue

            j,k=i+1,len(s)-1
            
            while j<k:
                t=s[i]+s[j]+s[k]
                print(i,j,k,t)
                if t==0: 
                    arr.append([s[i], s[j], s[k]])
                    while j<len(s)-1 and s[j]==s[j+1]: j+=1
                    while k>0 and s[k]==s[k-1]: k-=1
                    j+=1
                    k-=1
                elif t>0: k-=1
                else: j+=1
            i+=1
        return arr