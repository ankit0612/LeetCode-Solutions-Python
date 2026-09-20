class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # Find the first occurrence of the target
        def firstElement():

            # Start from the first index
            left = 0
            # Set right to the last index
            right = len(nums) - 1
            # Initially assume target is not found
            first = -1
            # Continue while a valid search range exists
            while left <= right:
                # Find the middle index
                mid = (left + right) // 2
                # Target found
                if nums[mid] == target:
                    # Save the current index
                    first = mid
                    # Continue searching on the left
                    # because there may be an earlier occurrence
                    right = mid - 1
                # Middle value is greater than target
                elif nums[mid] > target:
                    # Search on the left
                    right = mid - 1
                # Middle value is smaller than target
                else:
                    # Search on the right
                    left = mid + 1
            # Return first occurrence or -1
            return first

        # Find the last occurrence of the target
        def lastElement():

            # Start from the first index
            left = 0
            # Set right to the last index
            right = len(nums) - 1
            # Initially assume target is not found
            last = -1
            # Continue while a valid search range exists
            while left <= right:
                # Find the middle index
                mid = (left + right) // 2
                # Target found
                if nums[mid] == target:
                    # Save the current index
                    last = mid
                    # Continue searching on the right
                    # because there may be a later occurrence
                    left = mid + 1
                # Middle value is greater than target
                elif nums[mid] > target:
                    # Search on the left
                    right = mid - 1
                # Middle value is smaller than target
                else:
                    # Search on the right
                    left = mid + 1
            # Return last occurrence or -1
            return last

        # Find the first occurrence
        first = firstElement()
        # Find the last occurrence
        last = lastElement()
        # Return both positions
        return [first, last]