class Solution:
    # Function to find all possible paths
    def generateDirections(self, cur_row, cur_col, n):
        directions = [(cur_row + (cur_row+1 <= n), cur_col, 'D'),
                (cur_row, cur_col-(cur_col-1>=0), 'L'),
                (cur_row, cur_col + (cur_col+1 <= n), 'R'),
                (cur_row - (cur_row-1>=0),cur_col, 'U'),
                ];
                        
        return directions;
        
    def findPaths(self, cur_row, cur_col, des_row, des_col, path, paths, maze):
        if cur_row == des_row and cur_col == des_col:
            paths.append(path);
            return;
            
        directions = self.generateDirections(cur_row, cur_col, des_row);
        for i in range(len(directions)):
            row = directions[i][0];
            col = directions[i][1];
            direction = directions[i][2];
            if maze[row][col] != 0 and (row != cur_row or col != cur_col):
                path += directions;
                maze[cur_row][cur_col] = 0;
                self.findPaths(row, col, des_row, des_col, path, paths, maze);
                path = path[0:len(path)-1];
                maze[cur_row][cur_col] = 1;
        
        
    def ratInMaze(self, maze):
        # code here
        path = [];
        paths = [];
        n = len(maze[0])-1;
        if maze[n][n] == 0 or maze[0][0] == 0:
            return [];
        else:
            self.findPaths(0, 0, n, n, path, paths, maze);
            return paths;
            
