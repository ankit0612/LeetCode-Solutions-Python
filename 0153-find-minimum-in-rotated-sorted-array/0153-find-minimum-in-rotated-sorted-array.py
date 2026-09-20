class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Start the search from the first index
        left = 0
        # Set right to the last index
        right = len(nums) - 1
        # Continue until left and right point to the same position
        while left < right:
            # Find the middle index
            mid = (left + right) // 2
            # If middle value is greater than the right value,
            # the minimum must be somewhere to the right of mid
            if nums[mid] > nums[right]:
                # Move left pointer after mid
                left = mid + 1
            # Otherwise, the minimum is at mid or somewhere to its left
            else:
                # Keep mid in the search range
                right = mid
        # left == right, so this index contains the minimum
        return nums[left]