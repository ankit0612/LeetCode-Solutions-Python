#First Move: 
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(121)
#         l = int(str(s[::-1]))
#         if l == x:
#             return True
#         return False
        
# Second Move:
# with the classic way
class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp = x
        rev = 0

        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if temp == rev:
            return True
        return False