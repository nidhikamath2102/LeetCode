import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<=j:
            while i<len(s)-1 and not ('0'<=s[i].lower()<='9' or 'a'<=s[i].lower()<='z'):
                i+=1
            while j>0 and not ('0'<=s[j].lower()<='9' or 'a'<=s[j].lower()<='z'):
                j-=1
            if ('0'<=s[j].lower()<='9' or 'a'<=s[j].lower()<='z') and ('0'<=s[i].lower()<='9' or 'a'<=s[i].lower()<='z') and s[i].lower()!=s[j].lower(): return False
            i+=1
            j-=1
        return True