class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        def heapify(array, size, root):
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            if left < size and array[left] > array[largest]:
                largest = left
            if right < size and array[right] > array[largest]:
                largest = right
            if largest != root:
                array[root], array[largest] = array[largest], array[root]
                heapify(array, size, largest)

        for i in range(length // 2 - 1, -1, -1):
            heapify(nums, length, i)
        for i in range(length - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0] 
            heapify(nums, i, 0) 

        return nums
        