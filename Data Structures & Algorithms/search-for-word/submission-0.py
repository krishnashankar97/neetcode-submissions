class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c,i):
            #Base Case for True

            if i == len(word):
                return True
            
            #Base Case for Failure

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r + 1, c, i + 1) or  # Down
                     dfs(r - 1, c, i + 1) or  # Up
                     dfs(r, c + 1, i + 1) or  # Right
                     dfs(r, c - 1, i + 1))    # Left
            
            board[r][c] = temp

            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False
