class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum_value = numbers[left] + numbers[right]

            if sum_value < target:
                left += 1
            elif sum_value > target:
                right -= 1
            else:
                return [left + 1, right + 1]