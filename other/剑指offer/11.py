class Solution:
    def minArray(self, numbers) -> int:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if left == right:
                return numbers[left]

            mid = (left + right) // 2

            print(left, right)
            if numbers[mid] > numbers[right]:
                left = mid

            elif numbers[mid] > numbers[left]:
                right = mid

            elif numbers[right] > numbers[left]:
                left = mid

            elif numbers[right] <= numbers[right]:
                right = mid

        return numbers[left]


if __name__ == '__main__':
    print(Solution().minArray([3, 3, 1, 3]))
