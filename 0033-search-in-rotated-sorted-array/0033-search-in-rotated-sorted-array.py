class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Start the search from the first index
        left = 0
        # Set right to the last index
        right = len(nums) - 1
        # Continue searching while a valid range exists
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2
            # Check if the middle element is the target
            if nums[mid] == target:
                # Target found, return its index
                return mid
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                # Check if target belongs to the sorted left half
                if nums[left] <= target < nums[mid]:
                    # Search the left half
                    right = mid - 1
                # Target is not in the left sorted half
                else:
                    # Search the right half
                    left = mid + 1
            # Otherwise, the right half is sorted
            else:
                # Check if target belongs to the sorted right half
                if nums[mid] < target <= nums[right]:
                    # Search the right half
                    left = mid + 1
                # Target is not in the right sorted half
                else:
                    # Search the left half
                    right = mid - 1
        # Target was not found
        return -1