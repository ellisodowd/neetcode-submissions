class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            rowSet = set()
            colSet = set()
            for y in range(9):
                print(x%3, y%3)
                if board[x][y] != "." and board[x][y] in rowSet:
                    return False
                rowSet.add(board[x][y])
                if board[y][x] != "." and board[y][x] in colSet:
                    return False
                colSet.add(board[y][x])
                if x%3 == 0 and y%3 == 0:
                    print('wow')
                    miniRowSet = set()
                    miniColSet = set()
                    for i in range(3):
                        for j in range(3):
                            print(board[x+i][y+j])
                            if board[x+i][y+j] != "." and board[x+i][y+j] in miniRowSet:
                                return False
                            miniRowSet.add(board[x+i][y+j])
                            if board[y+i][x+j] != "." and board[y+i][x+j] in miniColSet:
                                return False
                            miniColSet.add(board[y+i][x+j])


        
        return True
                
        