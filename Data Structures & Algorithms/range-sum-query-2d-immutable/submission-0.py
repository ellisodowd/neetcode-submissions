class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        #compute horizontally
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    prefix = matrix[i][j]
                else:
                    prefix = matrix[i][j] + self.preMatrix[i+1][j]
                self.preMatrix[i + 1][j + 1] = prefix 
        for i in range(ROWS):
            for j in range(COLS):
                self.preMatrix[i + 1][j + 1] += self.preMatrix[i][j + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.preMatrix[row2 + 1][col2 + 1]
        - self.preMatrix[row1][col2 + 1]
        - self.preMatrix[row2 + 1][col1]
        + self.preMatrix[row1][col1])



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)