class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for ch in strs:
            key = tuple(sorted(ch))
            if key in dict:
                dict[key].append(ch)
            else:
                dict[key] = [ch]
        return list(dict.values())
        