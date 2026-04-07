class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip i duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            
            while left < right:
                triplet = nums[i], nums[left], nums[right]

                if sum(triplet) == 0:
                    res.append(triplet)
                    left += 1

                    # skip triplet duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif sum(triplet) < 0:
                    left += 1
                else:
                    right -= 1

        return res