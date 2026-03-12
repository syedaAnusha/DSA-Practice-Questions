class Solution:
    # Time Complexity: O(2n)
    # Space Complexity: O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [];
        N = len(asteroids);
        for i in range(N):
            if asteroids[i] > 0:
                stack.append(asteroids[i]);
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop();
                if stack and stack[-1] > 0 and abs(asteroids[i]) == stack[-1]:
                    stack.pop();
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i]);
        return stack;