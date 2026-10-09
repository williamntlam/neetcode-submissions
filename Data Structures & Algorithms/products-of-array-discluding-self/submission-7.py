class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix multiplications
        # [1, 2, 8, 40]
        # [1 , 48, 24, 6]

        # [ 1 8 40 ]
        # [ 6 48 48 ]
        # example: 24 is the answer for i=1
        # technically it would be the left most element * the right most element form the right.

        # naive approach: 
        # 1. loop through each num and find total multiplication total while leaving the current index
        # 2. save the computation in an array
        # the runtime complexity is O(n^2) since you loop through the array for each element
        # the spacetime complexity would be O(n) since the multiplication total is a single variable
        # and the answer array is N elements.

        # for the fast approach using prefix and suffix arrays, the runtime is O(n) since you only need to scan through the 
        # nums array once and then the once more.
        # runtime is O(n)
        # spacetime is O(n)

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        current_prefix = 1
        current_suffix = 1
        back = len(nums) - 1
        for front in range(len(nums)):
            current_prefix = current_prefix * nums[front]
            prefix[front] = current_prefix

            current_suffix = current_suffix * nums[back]
            suffix[back] = current_suffix

            back = back - 1

        answer = [1] * len(nums)
        for index in range(1, len(nums) - 1):
            answer[index] = prefix[index - 1] * suffix[index + 1]

        answer[0] = suffix[1]
        answer[-1] = prefix[-2]

        return answer