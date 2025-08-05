# User function Template for python3

class Solution:
    def isSafeToColor(self, currentColor,  graph, color, node, v):
        for k in range(v):
            if k != node and graph[k][node] == 1 and color[k] == currentColor:
                return False;
        return True;
       
        
        
    def findAllValidColorGraphs(self, v, m, color, graph, node):
        if node == v:
            return True;
            
        for i in range(1, m+1):
            if self.isSafeToColor(i, graph, color, node, v):
                color[node] = i;
                if self.findAllValidColorGraphs(v, m, color, graph, node+1):
                    return True;
                color[node] = 0;
                
        return False;
            
            
    def graphColoring(self, v, edges, m):
        # code here
        color = [0] * v;
        node = 0;
        graph = [[0]*v for i in range(v)];
        for value in edges:
            row = value[0];
            col = value[1];
            graph[row][col] = 1;
        
    
        #print('graph', graph);
        return self.findAllValidColorGraphs(v, m, color, graph, node);
        
        
        