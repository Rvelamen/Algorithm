class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(k > 0)
        print(id(nums))
        nums[:] = nums[len(nums) - (k % len(nums)): len(nums)] + nums[0:len(nums) - (k % len(nums))] if k % len(nums) != 0 or k == 0 else nums[::-1]
        print(id(nums))

x = Solution().rotate(
[1,2],
0)

