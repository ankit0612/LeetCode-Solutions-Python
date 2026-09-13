class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) -1
        vowels = set('aeiouAEIOU')
        newString = list(s)
        #travers until the length of string-> 
        while left < right:
            # if s[left] -> s[0] is not a vawel then move forward from left side (soimething like current is s[0] ->s[1] -> s[2] and so on)
            if s[left] not in vowels:
                # moving ahead from the left side
                left +=1
            # if s[right] -> s[7](that means the last element which is m in this string "IceCreAm") is not a vawel then move forward from right side (wheer we need to move backward soimething like current is s[7] ->s[6] -> s[5] and so on)
            elif s[right] not in vowels:
                # moving ahead from the right side
                right -=1
            else:
                # if both are vowels then we can swap them 
                # NOTE: we cant swap the original string we need to create a new string just as I do and assign that value to it for swaping later
                newString[left], newString[right] = newString[right], newString[left]
                # now we got the first match so we need to move forward from both side (left and right).
                left +=1
                right -=1
        # as we create a new variable name newString which is a list, for the result we need to convert it as a string -> for that we need to use join method.
        return ''.join(newString)