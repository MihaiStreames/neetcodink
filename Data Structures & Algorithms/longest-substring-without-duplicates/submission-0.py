class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, right = 0, 0
        res = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                window.remove(s[left])
                left += 1

        return res