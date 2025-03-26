class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for ch in strs:
            key = ''.join(sorted(ch))
            if key in dict.keys():
                dict[key].append(ch)
            else:
                dict[key] = [ch]
        return dict.values()
        