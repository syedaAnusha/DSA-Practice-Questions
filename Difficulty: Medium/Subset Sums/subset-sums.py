class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^n)*O(n)
    # Space Complexity: O(2^n) + O(2^n) for recursive calls, where k is the length of sumsArr
    def generateSubsetsSums(self,arr, sumsArr, index, Sum):
        #sumsArr.append(Sum);
        for i in range(index, len(arr)):
            curSum = Sum + arr[i];
            sumsArr.append(curSum);
            self.generateSubsetsSums(arr, sumsArr, i+1, curSum);
            #sumsArr.remove(curSum);
            
	def subsetSums(self, arr):
		# code here
		sumsArr = [0];
		index = 0;
		Sum = 0;
		self.generateSubsetsSums(arr, sumsArr, index, Sum);
		return sumsArr;