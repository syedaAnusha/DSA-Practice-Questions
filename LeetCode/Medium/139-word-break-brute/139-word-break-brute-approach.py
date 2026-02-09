class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def wordBreakHelper(self, s, dictionary, index):
        if index == len(s):
            return True;
            
        for i in range(index, len(s)):
            if s[index:i+1] in dictionary and self.wordBreakHelper(s, dictionary, i+1):
                return True;
        return False;

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        index = 0;
        return self.wordBreakHelper(s, wordDict, index);
