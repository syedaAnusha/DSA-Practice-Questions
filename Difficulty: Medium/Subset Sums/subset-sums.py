#User function Template for python3
class Solution:
    def findSubsetSums(self, arr, tempArr, ans, index):
        if index == len(arr):
            Sum = sum(tempArr)
            ans.append(Sum);
            return;
        else:
            tempArr.append(arr[index]);
            self.findSubsetSums(arr, tempArr, ans, index+1);
            tempArr.remove(arr[index]);
            self.findSubsetSums(arr, tempArr, ans, index+1);
            
	def subsetSums(self, arr):
		# code here
		ans = [];
		self.findSubsetSums(arr, [], ans, 0);
		return ans;