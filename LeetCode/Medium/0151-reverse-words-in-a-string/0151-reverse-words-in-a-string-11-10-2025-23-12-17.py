class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) * O(n) = O(n^2) 
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        wordsArr = s.split();
        n = len(wordsArr) - 1;
        reversedSentence = "";

        for i in range(n, -1, -1):
            reversedSentence += wordsArr[i]+' ';

        revStrLen = len(reversedSentence);
        return reversedSentence[:revStrLen-1];
