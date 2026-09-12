class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = {} 
        for row in range(9):
            row_seen = {}
            column_seen = {}

            for column in range(9):
                if board[row][column] != ".":
                    if board[row][column] in row_seen:
                        return False
                    row_seen[board[row][column]] = 1
                if board[column][row] != ".":
                    if board[column][row] in column_seen:
                        return False
                column_seen[board[column][row]] = 1
                box = (row // 3, column // 3)

                if box not in squares:
                    squares[box] = set()

                if board[row][column] != ".":
                    if board[row][column] in squares[box]:
                        return False

                    squares[box].add(board[row][column])
        return True