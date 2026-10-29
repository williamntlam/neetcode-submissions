class Solution:
    def trap(self, height: List[int]) -> int:
        # non decreasing or strictly decreasing monotonic stack?
        # either is fine.
        # for this algorithm it's always the last element that we use.

        # maybe use the wall to the left of it? as in take the min of both?
        # wait is this needed? we know the wall on the right is larger
        # than the ones on the left. maybe i could use this to my advantage.
        # the difference between the current height, the height saved on the stack
        # times the width maybe?
        # i think i need to use the left hand wall for this.
        # runtime O(n)
        # spacetime O(n)

        monotonic_stack = [] # non-increasing.
        area = 0

        for index in range(len(height)):
            current_height = height[index]

            while monotonic_stack and height[monotonic_stack[-1]] <= current_height:
                floor_index = monotonic_stack.pop()
                if not monotonic_stack:
                    break
                    
                left_wall = height[monotonic_stack[-1]]
                right_wall = current_height
                wall = min(left_wall, right_wall)

                width = index - monotonic_stack[-1] - 1
                area += width * (wall - height[floor_index])

            monotonic_stack.append(index)

        return area