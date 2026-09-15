class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create the result array.
        # Initially, assume there is no warmer day, so everything is 0.
        result = [0] * len(temperatures)
        # Stack will store the INDEXES of days
        # that are still waiting for a warmer temperature.
        stack = []
        # Go through each day from left to right.
        for i in range(len(temperatures)):
            # Check if:
            # 1. Stack is not empty
            # 2. Current temperature is warmer than the temperature
            #    of the day stored at the top of the stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Remove the previous day from the stack.
                # This day has now found its warmer day.
                previousDay = stack.pop()
                # Calculate how many days we had to wait.
                # Current day index - previous day index
                result[previousDay] = i - previousDay
            # Put the current day's INDEX into the stack.
            # This day may need to wait for a warmer day in the future.
            stack.append(i)

        # Return the number of days to wait for each day.
        return result