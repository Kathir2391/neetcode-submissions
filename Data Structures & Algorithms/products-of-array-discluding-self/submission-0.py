class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        output = [1] * nums_len

        prefix = 1
        for i in range(nums_len):
            output[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(nums_len-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
 
        