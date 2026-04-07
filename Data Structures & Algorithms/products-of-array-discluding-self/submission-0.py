class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            l_prod[i] = l_prod[i - 1] * nums[i - 1]

        r_prod = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):  # i forgot how these worked
            r_prod[i] = r_prod[i + 1] * nums[i + 1]

        return [l_prod[i] * r_prod[i] for i in range(len(nums))]