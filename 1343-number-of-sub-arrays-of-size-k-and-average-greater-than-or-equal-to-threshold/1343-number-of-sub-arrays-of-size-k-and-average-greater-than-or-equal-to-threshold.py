class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        # Counter to store the number of valid windows
        counter = 0
        # Left pointer starts at the beginning of the array
        left = 0
        # Right pointer starts at the end of the first window
        right = k - 1
        # Calculate the sum of the first window
        window_sum = sum(arr[:k])
        # Check if the first window's average meets the threshold
        if window_sum / k >= threshold:
            # Increase the counter when the window is valid
            counter += 1
        # Continue sliding the window while another element is available
        while right < len(arr) - 1:
            # Move the left pointer forward
            left += 1
            # Move the right pointer forward
            right += 1
            # Remove the element leaving the window and add the new element
            window_sum = window_sum - arr[left - 1] + arr[right]
            # Check if the current window's average meets the threshold
            if window_sum / k >= threshold:
                # Increase the counter when the window is valid
                counter += 1
        # Return the total number of valid windows
        return counter