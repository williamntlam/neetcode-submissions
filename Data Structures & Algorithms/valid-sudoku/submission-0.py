class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # naive approach:
        # for each cell with a number
        # look through the entire row to see if that number repeats
        # look through the entire column to see if that number repeats
        # look through it's 3x3 area to see if that number repeats
        # if any of the above are true, return false
        # keep doing this until you've scanned all cells with a number
        # runtime complexity: O(N^3)
        # spacetime complexity: O(n^2)

        # take advantage of hashing for O(1) look up times.
        # maybe separate the search into 3 entities to make it simple
        # is there a number in this row?
        # is there a number in this column?
        # is there a number in this 3x3 square?

        # runtime I'm aiming for: O(n^2). Check each cell at most once.

        row_check = { index: set() for index in range(0, 10) } # { row # : set() }
        column_check = { index: set() for index in range(0, 10) } # { col #: set() }
        three_by_three_square_check = { } # { square #: set() } should only be 9 squares.

        # populate these attributes
        # can do preliminary checks to see if a row, column, or square have 2 identical numbers

        for row_index in range(9):
            number_set = set()
            for col_index in range(9):
                current_number = board[row_index][col_index]
                if current_number != ".":
                    if current_number not in number_set:
                        number_set.add(current_number)
                    else:
                        return False
            row_check[row_index] = number_set

        for row_index in range(9):
            number_set = set()
            for col_index in range(9):
                current_number = board[col_index][row_index]
                if current_number != ".":
                    if current_number not in number_set:
                        number_set.add(current_number)
                    else:
                        return False
            column_check[col_index] = number_set

        # square check
        # 0-2 square 0
        # 3-5 square 1
        # 6-8 square 2
        # can just hardcode positions since it's always a 9x9 square.
        # better to just do floor division.
        for row_index in range(9):
            for column_index in range(9):
                current_number = board[row_index][column_index]
                if current_number != ".":
                    three_by_three_square = (row_index // 3, column_index // 3)
                    if three_by_three_square not in three_by_three_square_check:
                        three_by_three_square_check[three_by_three_square] = set(current_number)
                    else:
                        if current_number in three_by_three_square_check[three_by_three_square]:
                            return False
                        three_by_three_square_check[three_by_three_square].add(current_number)

        # standardize using floor division
        # just have a row and column index from 0-2 for each so a key index would be (x,y) for a 3x3 square check.
        
        return True

        