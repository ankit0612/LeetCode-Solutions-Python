class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        l = 0
        r = len(nums) -1
        pos = len(nums) -1

        while l <= r:
            if nums[l]**2 < nums[r]**2:
                result[pos] = nums[r]**2
                r -=1
                pos -=1
            else:
                result[pos] = nums[l]**2
                l +=1
                pos -=1
        return result
                
