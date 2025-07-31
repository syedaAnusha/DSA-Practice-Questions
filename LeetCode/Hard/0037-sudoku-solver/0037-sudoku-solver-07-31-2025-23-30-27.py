class Solution(object):
    def solveSudoku(self, board):
        # Track used numbers in rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and find empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(idx):
            if idx == len(empties):  # all cells filled
                return True

            r, c = empties[idx]
            box = (r // 3) * 3 + (c // 3)

            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box]:
                    # Place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box].add(ch)

                    if backtrack(idx + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box].remove(ch)

            return False

        backtrack(0)
