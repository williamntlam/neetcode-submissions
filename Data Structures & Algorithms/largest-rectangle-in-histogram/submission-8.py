class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monotonic_stack = []
        max_area = 0

        for index in range(len(heights) + 1):
            height = heights[index] if index < len(heights) else 0

            while monotonic_stack and heights[monotonic_stack[-1]] > height:
                popped_height = heights[monotonic_stack.pop()]

                if monotonic_stack:
                    width = index - monotonic_stack[-1] - 1
                else:
                    width = index

                max_area = max(max_area, popped_height * width)

            monotonic_stack.append(index)

        return max_area