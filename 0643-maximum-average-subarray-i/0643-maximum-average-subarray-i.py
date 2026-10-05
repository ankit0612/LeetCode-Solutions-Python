class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        # Calculate the sum of the first window
        window_sum = sum(nums[:k])
        # Initially, the first window is the maximum
        max_sum = window_sum
        # Start the left pointer at the beginning
        left = 0
        # Start the right pointer at the end of the first window
        right = k - 1
        # Continue while another element exists to enter the window
        while right < len(nums) - 1:
            # Move the right pointer forward
            right += 1
            # Move the left pointer forward
            left += 1
            # Remove the element that left and add the new element
            window_sum = window_sum - nums[left - 1] + nums[right]
            # Keep track of the maximum window sum
            max_sum = max(max_sum, window_sum)
        # Convert the maximum sum into an average
        return max_sum / k