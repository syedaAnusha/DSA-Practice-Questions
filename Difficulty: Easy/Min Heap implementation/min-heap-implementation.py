class minHeap:
    # Optimal Approach
    # Space Complexity: O(100)
    MEMORY = 10**5;
    
    def __init__(self):
        # Initialize your data members
        self.length = 0;
        self.arr = [0] * self.MEMORY;
        
    
    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i];
        
    
    def parent(self, index):
        return (index-1) // 2;
        
    # Insert x into the heap
    # T.C = O(log n)
    def push(self, x: int):
        # code here
        if self.length == 0:
            self.arr[0] = x;
            self.length += 1;
            return;
            
        index = self.length;
        self.arr[index] = x;
        self.length += 1;
        
        while index > 0 and self.arr[self.parent(index)] > self.arr[index]:
            self.swap(self.parent(index), index, self.arr);
            index = self.parent(index);
        
    
    # T.C = O(log n)
    def heapify(self, index):
        smallest = index;
        left = 2*index+1;
        right = 2*index+2;
        
        if left < self.length and self.arr[left] < self.arr[smallest]:
            smallest = left;
        if right < self.length and self.arr[right] < self.arr[smallest]:
            smallest = right;
        
        if smallest != index:
            self.swap(smallest, index, self.arr);
            self.heapify(smallest);
            
    # Remove the top (minimum) element
    # T.C = O(log n)
    def pop(self):
        # code here
        if self.length <= 0:
            return float("-inf");
        
        if self.length == 1:
            self.length -= 1;
            return self.arr[0];
            
        self.arr[0] = self.arr[self.length-1];
        self.length -= 1;
        self.heapify(0);
       
        
    # Return the top element or -1 if empty
    # T.C = O(1)
    def peek(self) -> int:
        # code here
        #("arr", self.arr);
        if self.length >= 1:
            return self.arr[0];
        return -1;


    # Return the number of elements in the heap
    # T.C = O(1)
    def size(self) -> int:
        # code here
        return self.length;