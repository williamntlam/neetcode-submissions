class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # naive approach: do a double for loop
        # can compute all the possible combinations.
        # and the resulting longest sequence
        # runtime complexity: O(n^2)
        # spacetime complxity: O(n)

        # a more optimized approach:
        # maybe there's a more simple approach
        # if i can efficiently count how many
        # elements that are greater to the right
        # of an index that might be good enough

        # I think I could convert it into a set and then go through each index.

        # current approach
        # runtime: O(4n) = O(n) 
        # spacetime: O(n)

        if nums == []:
            return 0

        # consecutive sequence, exactly 1 greater.
        nums_set = set(nums)

        longest_consecutive_length = 1
        current_consecutive_length = 1
        for number in nums_set:
            current_consecutive_length = 1
            if number - 1 not in nums_set:
                current_number = number
                while current_number + 1 in nums_set:
                    current_number += 1
                    current_consecutive_length += 1
            longest_consecutive_length = max(longest_consecutive_length, current_consecutive_length)

        return longest_consecutive_length