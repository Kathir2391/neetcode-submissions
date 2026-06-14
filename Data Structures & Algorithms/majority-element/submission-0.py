from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurence = Counter(nums)
        return occurence.most_common(1)[0][0]