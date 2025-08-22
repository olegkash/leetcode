class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        minRow, minCol = ROWS, COLS
        maxRow, maxCol = -1, -1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    minRow = min(minRow, r)
                    minCol = min(minCol, c)
                    maxRow = max(maxRow, r)
                    maxCol = max(maxCol, c)
        
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)
