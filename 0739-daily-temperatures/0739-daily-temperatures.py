class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)-1
        answer,st=[0]*n,[n]
        for i in range(n-1,-1,-1):
            while len(st)>0 and temperatures[i]>=temperatures[st[-1]]: 
                st.pop()
            if len(st)>0: answer[i]=st[-1]-i
            st.append(i)
        return answer