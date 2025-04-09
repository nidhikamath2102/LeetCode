class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch not in {"+", "-", "*", "/"}: 
                st.append(int(ch))
            else:
                v1=st.pop()
                if len(st)>0: v2=st.pop()
                else: v2=0
                if ch=="+": v=v2+v1
                elif ch=="-": v=v2-v1
                elif ch=="*": v=v2*v1
                else: v=v2/v1
                st.append(int(v))
        return int(st[-1])