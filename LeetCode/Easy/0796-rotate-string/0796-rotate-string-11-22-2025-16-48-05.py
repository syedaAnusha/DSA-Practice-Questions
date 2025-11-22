class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rotateString(self, s: str, goal: str) -> bool:
        doubledS = s + s;
        if len(s) == len(goal) and goal in doubledS:
            return True;
        return False;