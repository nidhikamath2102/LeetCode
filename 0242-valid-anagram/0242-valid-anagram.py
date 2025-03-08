class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        
        arr={}
        for i in s:
            arr[i] = arr.get(i, 0) + 1
        
        for i in t:
            if i in arr:
                arr[i] = arr.get(i,0) - 1
                if arr[i] == 0:
                    arr.pop(i)
        return len(arr) == 0