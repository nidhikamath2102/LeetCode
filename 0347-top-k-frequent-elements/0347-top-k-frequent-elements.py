class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        arr=[[] for i in range(len(nums)+1)]
        topk=[]

        for n in nums:
            freq[n]=freq.get(n, 0)+1

        for i,n in freq.items():
            arr[n].append(i)

        for i in range(len(arr)-1,-1,-1):
            for n in arr[i]:
                topk.append(n)
                if len(topk)==k:
                    return topk