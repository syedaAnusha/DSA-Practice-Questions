class Solution(object):
    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def findPermutations(self, arr, ds, index, ans):
        if index == len(arr):
            ans.append(list(ds));
            return;
        else:
            for i in range(index, len(arr)):
                self.swap(ds, index, i);
                self.findPermutations(arr, ds, index+1 , ans);
                # re-swap
                self.swap(ds, index, i);
                
                
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # An Approach2 with swap - 0(1) 
        ans = [];
        ds = nums;
        index = 0;
        self.findPermutations(nums, ds, index, ans);
        return ans;
        