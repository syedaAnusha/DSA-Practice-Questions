class Solution(object):
    def findSubsets(self, arr, index, tempArr, ans):
        ans.append(list(tempArr));
        for i in range(index, len(arr)):
            tempArr.append(arr[i]);
            self.findSubsets(arr, i+1, tempArr, ans);
            tempArr.remove(arr[i]);

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        tempArr = [];
        index  = 0;
        self.findSubsets(nums, index, tempArr, ans);
        return ans;
        