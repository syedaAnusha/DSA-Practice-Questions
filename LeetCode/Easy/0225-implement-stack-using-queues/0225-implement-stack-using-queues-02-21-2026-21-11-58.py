from collections import deque
# Time Complexity: O(n) + O(1)
# Space Complexity: O(n), where n is the number pushed to queue
class MyStack:
    def __init__(self):
        self.que = deque();

    def push(self, x: int) -> None:
        qSize = len(self.que);
        self.que.append(x);
        for _ in range(qSize):
            self.que.append(self.que[0]);
            self.que.popleft();
    def pop(self) -> int:
        return self.que.popleft();
        
    def top(self) -> int:
        if len(self.que) != 0:
            return self.que[0];
        else:
            return 0;
        
    def empty(self) -> bool:
        if len(self.que) == 0:
            return True;
        return False;

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()