class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            if target - num in seen:
                return [min(index, seen[target - num]), max(index, seen[target - num])]
            seen[num] = index

        return False

        # Runtime is O(n) since we loop through each element once
        # average lookup time in the set is O(1)