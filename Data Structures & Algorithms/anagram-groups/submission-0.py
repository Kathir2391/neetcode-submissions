class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = []
        grouped_anagrams = {}
        for str in strs:
            sorted_string = "".join(sorted(str))
            if sorted_string in grouped_anagrams:
                grouped_anagrams[sorted_string].append(str)
            else:
                grouped_anagrams[sorted_string] = [str]
        final_result.extend(grouped_anagrams.values())
        return final_result
        