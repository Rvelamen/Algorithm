class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        mid = math.ceil((i + j) / 2)
        while i < j:
            if nums[mid] == target:
                break
            elif nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
            mid = math.ceil((i + j) / 2)

        if mid >= len(nums) or nums[mid] != target:
            return -1
        return mid

