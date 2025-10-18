# User function Template for python3
class Solution:
    # Optimal Approach
    # Time Complexity: O((N^m) * v) + O(V^2)
    # Space Complexity: O(V^2) = for matrix + O(N) = color array + O(N) = for aux space 
    def isSafetoInsertColor(self, matrix, index, colorArr, v, color):
        for k in range(v):
            if matrix[index][k] == 1 and index != k and colorArr[k] == color:
                return False;
        return True;
        
                
    def findColorGraph(self, matrix, colorArr, v, m, index):
        if index == v:
            return True;
        else:
            for color in range(1, m+1):
                if self.isSafetoInsertColor(matrix, index, colorArr, v, color):
                    colorArr[index] = color;
                    if self.findColorGraph(matrix, colorArr, v, m, index+1):
                        return True; 
                    colorArr[index] = 0;
                        
        return False;
        
    
    def graphColoring(self, v, edges, m):
        # code here
        # define matrix of v x v 
        matrix = [[0 for _ in range(v)] for _ in range(v)];
        
        # assign edges in matrix 
        for edge in edges:
            row = edge[0];
            col = edge[1];
            matrix[row][col] = 1;
        
        colorArr = [0 for _ in range(v)];
        index = 0;
        return self.findColorGraph(matrix, colorArr, v, m, index);