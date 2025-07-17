class Solution(object):
    def findPermutations(self, arr, ds, index, ans, mapArr):
        if index == len(arr):
            ans.append(list(ds));
            return;
        else:
            for i in range(0, len(arr)):
                if mapArr[i] == 0:
                    ds.append(arr[i]);
                    mapArr[i] = 1;
                    self.findPermutations(arr, ds, index+1, ans, mapArr);
                    mapArr[i] = 0;
                    ds.remove(arr[i]);
                
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        ds = [];
        mapArr = [0] * len(nums);
        index = 0;

        self.findPermutations(nums, ds, index, ans, mapArr);
        return ans;
        