class Solution:
    def equal(self, ch1, ch2):
        return (ch1=='(' and ch2==')') or (ch1=='[' and ch2==']') or (ch1=='{' and ch2=='}')

    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if len(stack)==0 or not self.equal(stack[-1], ch): 
                stack.append(ch)
            elif self.equal(stack[-1], ch): 
                stack.pop()
        return len(stack)==0