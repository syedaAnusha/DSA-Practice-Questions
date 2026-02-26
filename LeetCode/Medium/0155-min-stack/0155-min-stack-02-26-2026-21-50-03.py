class MinStack:
    # Brute Force Approach
    # Time Complexity: O(1)
    # Space Complexity: O(2n)
    def __init__(self):
        self.stack = [];
        
    def push(self, val: int) -> None:
        if not self.stack:
            pair = (val,val);
            self.stack.append(pair);
        else:
            minVal = min(val, self.stack[-1][1]);
            pair = (val, minVal);
            self.stack.append(pair);

    def pop(self) -> None:
        return self.stack.pop();

    def top(self) -> int:
        topVal = self.stack[-1];
        return topVal[0];
        
    def getMin(self) -> int:
        curMinVal = self.stack[-1];
        return curMinVal[1];
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()