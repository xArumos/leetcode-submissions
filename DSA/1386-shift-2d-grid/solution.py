class Solution:
    def build1D(self, grid: List[List[int]]) -> List[int]:
        result = []

        for i in grid:
            for j in i:
                result.append(j)

        return result
    def build2D(self, flatGrid: List[int], rows: int, cols: int) -> List[List[int]]:
        grid = [[0 for i in range(cols)] for j in range(rows)]

        for row in range(rows):
            for col in range(cols):
                grid[row][col] = flatGrid[col + (cols * row)]

        return grid
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatGrid = self.build1D(grid)
        rows = len(grid)
        cols = len(grid[0])

        for i in range(k):
            flatGrid.insert(0, flatGrid[-1])
            flatGrid.pop()

        result = self.build2D(flatGrid, rows, cols)

        return result
