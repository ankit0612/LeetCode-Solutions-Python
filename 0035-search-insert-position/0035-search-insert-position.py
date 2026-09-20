class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # Start the search from the first index
        left = 0
        # Set right to the last index
        right = len(nums) - 1
        # Continue while there is a valid search range
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            # Check if the middle element is the target
            if nums[mid] == target:
                # Target found, return its index
                return mid
            # If middle value is greater than target,
            # search in the left half
            elif nums[mid] > target:
                # Move right before mid
                right = mid - 1
            # If middle value is smaller than target,
            # search in the right half
            else:
                # Move left after mid
                left = mid + 1
        # Target was not found.
        # left is the correct insertion position.
        return left