import string;
class Solution:
    # Optimal Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)  
    def beautySum(self, s: str) -> int:
        sumOfSubStrs = 0;
        n = len(s);
    
        for i in range(n):
            freq = [0] * 26;
            for j in range(i,n):
                index = ord(s[j]) - ord('a');
                freq[index] += 1;
                maxFreq = 0;
                minFreq = float('inf');
                for f in freq:
                    if f > 0:
                        maxFreq = max(maxFreq, f);
                        minFreq = min(minFreq, f);
                sumOfSubStrs += (maxFreq - minFreq);
        return sumOfSubStrs;

        