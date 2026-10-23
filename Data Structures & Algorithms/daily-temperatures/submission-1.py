class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # start with brute force.
        # O(n^2) - just have two for loops and check for each index
        # the next biggest element.
        # now, let's try to find a better solution (i.e better than O(n^2))
        # think about O(nlogn), O(n), O(1) seems pretty impossible
        # what related things do we know about O(nlogn)
        # well... binary search and heaps are O(logn)
        # for O(n), a constant # of linear scans.
        # two pointers / sliding windows are typically O(n)
        # for the O(nlogn) solution, you could just sort from smallest to largest value and
        # monotonic stack?

        # [0] -> 38 is the current
        # [1] -> 30 is the new current.
        # [1,2 ] -> 36 is the new current
        # [1,3] -> 35 is the new current
        # [1,4] -> 40 is the new current
        # [5] -> 28 is the new current

        # attempt to do monotonic stack solution in O(n) time.
        # runtime complexity: O(n)
        # spacetime: O(n)
        monotonic_stack = []
        result = [0 for _ in range(len(temperatures))]

        for index, temperature in enumerate(temperatures):
            while monotonic_stack and temperatures[monotonic_stack[-1]] < temperature:
                result[monotonic_stack[-1]] = index - monotonic_stack[-1]
                monotonic_stack.pop()

            monotonic_stack.append(index)
            
        return result