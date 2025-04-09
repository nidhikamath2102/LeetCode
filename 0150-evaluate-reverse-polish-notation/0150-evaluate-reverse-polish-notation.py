class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch not in {"+", "-", "*", "/"}: 
                st.append(int(ch))
            else:
                v1,v2=st.pop(),st.pop()
                if ch=="+": st.append(v1+v2)
                elif ch=="-": st.append(v2-v1)
                elif ch=="*": st.append(v1*v2)
                else: st.append(int(v2/v1))
        return int(st[-1])