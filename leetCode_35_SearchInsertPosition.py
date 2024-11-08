class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def serachInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        # somehow returning low is enough, a small modification.
        return low
