class Solution(object):
    def func0(self, numbers, target):
        """
        普通二分查找
        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            elif numbers[mid] > target:
                right = mid - 1
        return -1

    def func1(self, numbers, target):
        """
        查找第一个与key相等的元素

        :param numbers:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1
            if numbers[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left >= 0 and left < len(numbers) and numbers[left] == target:
            return left

        return -1

    def func2(self, numbers, target):
        """
        查找最后一个与key相等的元素
        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1

            if numbers[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0 and right < len(numbers) and numbers[right] == target:
            return right

        return -1

    def func3(self, numbers, target):
        """
        查找最后一个等于或者小于key的元素

        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1

            if numbers[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def func4(self, numbers, target):
        """
        查找最后一个小于key的元素

        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1

            if numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def func5(self, numbers, target):
        """
        查找第一个等于或者大于key的元素

        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1

            if numbers[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def func6(self, numbers, target):
        """
        查找第一个大于key的元素

        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) >> 1

            if numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().func6([1, 4, 7, 9, 10], target=6))
