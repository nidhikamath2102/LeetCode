class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==1: return 1
        ps=list(zip(position,speed))
        ps.sort(reverse=True)

        c=1
        current=(target-ps[0][0])/ps[0][1]

        for i in range(1, len(ps)):
            t = (target-ps[i][0])/ps[i][1]
            if t>current:
                current=t
                c+=1
        return c