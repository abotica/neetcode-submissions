class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for i in range(9):
            # for each row create a set
            row = set()
            for j in range(9):
                # check if row is unique, if element is '.' ignore it
                if board[i][j] in row:
                    return False # validator failed, all need to be unique
                elif board[i][j] != ".":
                    row.add(board[i][j])

        # columns
        for i in range(9):
            # for each column create a set
            column = set()

            for j in range(9):
                if board[j][i] in column:
                    return False
                elif board[j][i] != ".":
                    column.add(board[j][i])

        # boxes
        # because sudoku is fixed size we can actually hard code the starting indices of each box

        starts = [(0,0), (0,3), (0, 6),
                 (3, 0), (3,3), (3, 6),
                 (6,0), (6,3), (6,6)]

        for i, j in starts:
            box = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] in box:
                        return False
                    elif board[x][y] != ".":
                        box.add(board[x][y])

        return True






