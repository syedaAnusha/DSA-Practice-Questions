class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def vowelConsonantScore(self, s: str) -> int:
        consonantsCount = 0;
        vowelsCount = 0;
        score = 0;
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        for char in s:
            if char.isspace() or char.isdigit():
                continue;
            elif char in vowels:
                vowelsCount += 1;
            else:
                consonantsCount += 1;
        if consonantsCount > 0:
            score = math.floor(vowelsCount / consonantsCount);
            return score;
        return score;