import re
class Solution:
    def checkAlphaNumeric(self, c):
        return ('0'<=c.lower()<='9' or 'a'<=c.lower()<='z')

    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<=j:
            while i<j and not self.checkAlphaNumeric(s[i]): i+=1
            while j>i and not self.checkAlphaNumeric(s[j]): j-=1
            if i<=j and s[i].lower()!=s[j].lower(): return False
            i,j=i+1,j-1
        return True