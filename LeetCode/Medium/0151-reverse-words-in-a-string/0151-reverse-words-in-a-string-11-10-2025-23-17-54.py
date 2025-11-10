class Solution:
    # Better Approach
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]);
