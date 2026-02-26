class MinStack:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def __init__(self):
        self.stack = [];
        self.minVal = float('inf');
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val);
            self.minVal = val;
        else:
            if val > self.minVal:
                self.stack.append(val);
            else:
                newVal = 2*val - self.minVal;
                self.stack.append(newVal);
                self.minVal = val;

    def pop(self) -> None:
        if not self.stack:
            return;
        val = self.stack.pop();
        if val < self.minVal:
            self.minVal = 2*self.minVal - val;
        return val;

    def top(self) -> int:
        if not self.stack:
            return;
        if self.stack[-1] < self.minVal:
            return self.minVal;
        return self.stack[-1];
        
    def getMin(self) -> int:
        return self.minVal;
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()