class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {']': '[', '}': '{', ')': '('}
        stack = []
        for char in s:
            if char in mapper.values():
                stack.append(char)
            elif char in mapper.keys():
                if not stack or mapper[char] != stack.pop():
                    return False
        # return True
        return len(stack) == 0