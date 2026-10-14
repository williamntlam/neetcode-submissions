class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution use O(1) additional space.
        # algorithm -> need to search through the space
        # since this array is sorted, have a left and right pointer
        # if th target is grater than the current sum, move the right pointer left
        # otherwise move the left pointer right

        # runtime is O(n)
        # spacetime complexity is O(1)

        left = 0
        right = len(numbers) - 1

        while left <= right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                break

        return [left + 1, right + 1]