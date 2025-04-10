class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer, n = [0], len(temperatures)-1
        st=[n]
        for i in range(n-1,-1,-1):
            
            if temperatures[i]<temperatures[st[-1]]:
                answer.insert(0,st[-1]-i)
                st.append(i)
                print("Inside If = ", temperatures[i], temperatures[st[-1]], st[-1])
            else:
                while len(st)>0 and temperatures[i]>=temperatures[st[-1]]: 
                    st.pop()
                if len(st)>0: answer.insert(0,st[-1]-i)
                else: answer.insert(0, 0)
                st.append(i)
                print("Inside else = ", temperatures[i], temperatures[st[-1]], st[-1])
        return answer