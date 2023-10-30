class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = (
            [nums[0]] + [0]*(n-1),
            [0]*(n-1) + [nums[-1]]
        )

        for x in range(1, n):
            pre[x], suf[n-x-1] = (
                pre[x-1] * nums[x],
                suf[n-x] * nums[n-x-1]
            )

        return (
            [suf[1]] +
            [pre[x-1] * suf[x+1] for x in range(1, n-1)] +
            [pre[-2]]
        )