class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^n)
    # Space Complexity: O(2^n) + O(n) for recursive calls
    def generateSubsetsSums(self,arr, sumsArr, index, Sum):
        for i in range(index, len(arr)):
            curSum = Sum + arr[i];
            sumsArr.append(curSum);
            self.generateSubsetsSums(arr, sumsArr, i+1, curSum);
            
	def subsetSums(self, arr):
		# code here
		sumsArr = [0];
		index = 0;
		Sum = 0;
		self.generateSubsetsSums(arr, sumsArr, index, Sum);
		return sumsArr;
