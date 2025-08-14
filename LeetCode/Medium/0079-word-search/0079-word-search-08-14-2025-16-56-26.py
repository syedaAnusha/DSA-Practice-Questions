class Solution:
    # Brute Force Approach
    # T.C = O(N*M*L*3^L)
    # S.C = O(N*M) + O(L) ≈ o(N*M) - in worst-case
    # Find all indexes (row, col) that starts with first word's character
    def findFirstCharacterIndex(self, arr, word):
        charArrayIndices = [];
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col] == word[0]:
                    charArrayIndices.append((row,col));
        return charArrayIndices; 

    # Generate all possible 4 directions DLRU.
    def generateDirections(self, row, col, n, m, arr):
        directions = [
            (row + (row+1 < m), col),
            (row, col - (col-1 >=  0)),
            (row, col + (col+1 < n)),
            (row - (row-1 >=  0),col),
            ];
        return directions;

    def findWord(self, arr, row, col, n, m, temp, word, index):
        if word == temp:
            return True;

        directions = self.generateDirections(row, col, n, m, arr);
        for i in range(len(directions)):
            nextRow = directions[i][0];
            nextCol = directions[i][1];
            value = arr[row][col];
            
            if (nextRow != row or nextCol != col) and arr[nextRow][nextCol] == word[index] and arr[nextRow][nextCol] != '0' and temp != word:
                arr[row][col] = '0';
                temp += word[index];
                if self.findWord(arr, nextRow, nextCol, n, m, temp, word, index+1):
                    return True;
                temp = temp[:len(temp)-1];
                arr[row][col] = value;
        return False;
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board);
        n = len(board[0]);
        index = 0;
        firstCharList = self.findFirstCharacterIndex(board, word);
        for value in firstCharList:
            temp = '';
            temp += word[0];
            if self.findWord(board, value[0], value[1], n, m, temp, word, 1):
                return True;
        return False;
        