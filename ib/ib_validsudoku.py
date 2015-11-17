'''VALIDSUDOKUBookmark
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem'''


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, board):
        char2int = {".":0, "1":1, "2":2, "3":4, "4":8, "5":16, "6":32, "7":64, "8":128, "9":256}
        board = [[char2int[item] for item in line] for line in board]
 
        # Check each row
        for i in range(9):
            sum  = 0
            for value in board[i]:
                if sum & value != 0:                return False
                sum = sum | value
                
        # Check each column
        for i in range(9):
            sum = 0
            for row in range(9):
                if sum & board[row][i] != 0:     return False
                sum = sum | board[row][i]
        
        # Check each block
        for iBlock in range(3):
            for jBlock in range(3):
                sum = 0
                for i in range(3):
                    for j in range(3):
                        if sum & board[iBlock*3+i][jBlock*3+j] != 0:    return False
                        sum = sum | board[iBlock*3+i][jBlock*3+j]
        
        return True
