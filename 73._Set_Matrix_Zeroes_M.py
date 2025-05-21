from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_zero = True
                    if c == 0:
                        first_col_zero = True

                    matrix[r][0] = 0
                    matrix[0][c] = 0

        
        for r in range(1,ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLS):
                    matrix[r][c] = 0

        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0    
