class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find eating rate of bananas-per-hour of k
        # want to find: minimum number of k such that you can eat
        # all bananas within h hours.
        
        # sum up all bananas.
        # do binary search with the lowest and highest num of bananas
        # keep trying to find the lowest value.

        # runtime: O(n * Logm) m = max # of bananas in a pike
        # spacetime: O(1)

        total_bananas = 0
        min_bananas = 1
        max_bananas = float('-inf')

        for pile in piles:
            min_bananas = min(min_bananas, pile)
            max_bananas = max(max_bananas, pile)
            total_bananas += pile

        while min_bananas <= max_bananas:
            mid = (min_bananas + max_bananas) // 2
            
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                max_bananas = mid - 1
            else:
                min_bananas = mid + 1
        
        return min_bananas