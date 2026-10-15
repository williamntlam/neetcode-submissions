class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # approach: Have a double for loop that
        # goes through all possible height combinations
        # save the max area formed.
        # runtime O(n^2)
        # spacetime: O(1)

        # optimized approach:
        # use a two pointers approach
        # we want to make the walls as high as possible
        # maybe have a left and right pointer
        # only decrement the side with the shorter height.
        # that way we always maximize the area.
        # runtime complexity: O(n)
        # spacetime: O(n)

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, current_area)

            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1

        return max_area