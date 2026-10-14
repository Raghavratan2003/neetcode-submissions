class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            col = []

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])

        for r in range(0,9,3):
            for c in range(0,9,3):
                box = []

                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] != ".":
                            if board[i][j] in box:
                                return False
                            box.append(board[i][j])

        return True