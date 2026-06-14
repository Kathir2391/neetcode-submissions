class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, number in enumerate(nums):
            reminder = target - number
            if reminder in lookup:
                return [lookup[reminder],index]
            lookup[number] = index
        