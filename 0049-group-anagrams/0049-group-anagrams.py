class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp={}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            ch=tuple(count)
            if ch not in grp:
                grp[ch] = [word]
            else:
                grp[ch].append(word)
        return tuple(grp.values())