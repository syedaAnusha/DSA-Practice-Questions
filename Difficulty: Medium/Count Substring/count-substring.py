#User function Template for python3

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countSubstring(self, s):
        # Code here
        count = {'a':0, 'b':0, 'c':0};
        validCnt = 0;
        n = len(s);
        left = 0;  
        
        for right in range(n):
            count[s[right]] += 1;
            
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                validCnt += (n-right);
                
                count[s[left]] -= 1;
                left += 1;
        return validCnt;