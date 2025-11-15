#User function Template for python3
class Solution:
    # Optimal Approach
    # Time Complexity: O(no: of set bits)
    # Space Complexity: O(1)
	def setBits(self, n):
		# code here
		setBitCnt = 0;
		while n > 0:
		    n = n & (n - 1);
		    setBitCnt += 1;
		return setBitCnt;