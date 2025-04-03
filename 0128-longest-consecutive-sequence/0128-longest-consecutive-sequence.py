class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        n_set = set(nums)
        curr_streak=1
        max_streak=1
        for n in n_set:
            if n+1 not in n_set:
                p=n
                curr_streak=1
                while p-1 in n_set:
                    curr_streak+=1
                    if curr_streak>max_streak:
                        max_streak=curr_streak
                    p-=1
        return max_streak
