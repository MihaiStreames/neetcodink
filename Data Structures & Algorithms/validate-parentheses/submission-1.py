class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = { ')': '(', '}': '{', ']': '[' }

        for char in s:
            if char in matching:  # closing bracket
                if not stack:
                    return False
                
                top = stack.pop()
                if top != matching[char]:
                    return False
            else:                 # opening bracket
                stack.append(char)

        return not stack  # must be empty