class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three pointers perhaps?
        # Naive approach:
        # runtime complexity: O(n^3)
        # have a triple for loop
        # spacetime complexity: O(n). Have a set to check for duplicate triplets.

        # Optimized Approach: 
        # runtime is O(n^2) since it's 1 + 2 + 3 + ... + n = n(n+1) / 2 = O(n^2)
        # spacetime is O(n) since i store all the triplets.
        # Imagine this, you could compute all triplets and check if it equals 0.
        # another better way would probably be to skip out on those that you know won't contribute
        # to the final answer.
        # how about we sort the array first?
        # e.x [-4,-1,-1,0,1,2]

        # left pointer, right pointer.
        # increase value, increase left pointer
        # decrease value, decrease right pointer
        # now i need the last pointer.
        # how about I make a set of the middle elements? I can simply add and remove elements in the 
        # set and have an average lookup time of O(1).

        # could i also just decrease the left and right pointers and iterate through the middle?
        # that might work. i don't want to miss any valid combinations.

        nums.sort()

        triplets = []

        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1

            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                middle_num = nums[index]

                total = left_num + right_num + middle_num

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([left_num, middle_num, right_num])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return triplets
