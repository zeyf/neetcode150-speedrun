class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index, num in enumerate(nums):
            if target - num in complements:
                return [
                    complements[target - num],
                    index
                ]
            elif num not in complements:
                complements[num] = index