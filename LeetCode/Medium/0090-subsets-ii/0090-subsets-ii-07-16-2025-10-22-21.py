class Solution(object):
    def findSubsets(self, arr, index, ans, tempArr):
        ans.append(list(tempArr))
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i-1]:
                continue;
            tempArr.append(arr[i]);
            self.findSubsets(arr, i+1, ans, tempArr);
            tempArr.remove(arr[i]);
        
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        nums.sort();
        self.findSubsets(nums, 0, ans, []);
        return ans;
        