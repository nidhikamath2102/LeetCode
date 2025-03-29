class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp={}
        for n in strs:
            ch=tuple(sorted(n))
            if ch not in grp:
                grp[ch] = [n]
            else:
                grp[ch].append(n)
        return tuple(grp.values())