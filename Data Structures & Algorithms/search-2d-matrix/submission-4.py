class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on first column
        # then binary search on the row.
        # runtime complexity: O(log(m) + log(n))) = O(log(m * n))
        # spacetime complexity: O(1)            

        top = 0
        bottom = len(matrix) - 1

        row_index = -1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            current_element = matrix[mid][0]

            if current_element < target:
                top = mid + 1
                row_index = mid
            
            if current_element > target:
                bottom = mid - 1

            if current_element == target:
                return True

        if row_index == -1:
            return False

        left = 0
        right = len(matrix[row_index]) - 1
        while left <= right:
            mid = (left + right) // 2
            middle_element = matrix[row_index][mid]

            if middle_element < target:
                left = mid + 1
            
            elif middle_element > target:
                right = mid - 1

            elif middle_element == target:
                return True

        return False
