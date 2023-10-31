class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                triplet_sum = nums[index] + nums[left] + nums[right]

                if triplet_sum < 0:
                    left += 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    triplet = [
                        nums[index],
                        nums[left],
                        nums[right]
                    ]

                    if len(triplets) > 0:
                        if triplets[-1] != triplet:
                            triplets.append(triplet)
                    else:
                        triplets.append(triplet)
                    
                    left, right = left + 1, right - 1

        return triplets