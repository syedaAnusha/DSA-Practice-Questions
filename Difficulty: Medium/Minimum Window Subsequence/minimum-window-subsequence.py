class Solution:
    # Better Approach
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)

    def minWindow(self, s1, s2):
        # Code here
        minSubsequence = "";
        i = j = 0;
        minLen = float("inf");
        
        while i < len(s1):
            if s1[i] == s2[j]:
                j += 1;
                
                if j == len(s2):
                    j -= 1;
                    endIndex = i;
                    
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1;
                        i -= 1;
                    
                    startIndex = i+1;
                    currLen = endIndex - startIndex + 1; 
                    if currLen < minLen:
                        minLen = currLen;
                        minSubsequence = s1[startIndex:endIndex+1];
                    i = startIndex;
                    j = 0;
            
            i += 1;
        return minSubsequence;