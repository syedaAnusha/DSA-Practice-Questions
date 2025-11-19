#User function Template for python3

class Solution:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def findXORTillN(self, N):
        remainder = N % 4;
        if remainder == 1:
            return 1;
        elif remainder == 2:
            return N+1;
        elif remainder == 3:
            return 0;
        elif remainder == 0:
            return N;
            
    def findXOR(self, l, r):
        # Code here
        ans = self.findXORTillN(l-1) ^ self.findXORTillN(r);
        return ans;