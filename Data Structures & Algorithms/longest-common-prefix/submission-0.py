class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        
        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last):
            if first[i] != last[i]:
                break
            i = i+1

        return first[:i]


