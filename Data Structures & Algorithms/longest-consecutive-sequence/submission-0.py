class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set()

        for n in nums:
            num_set.add(n)

        for n in nums:
            if n - 1 not in num_set:
                length = 0

                while (n + length) in num_set:
                    length += 1

                res = max(res, length)

        return res