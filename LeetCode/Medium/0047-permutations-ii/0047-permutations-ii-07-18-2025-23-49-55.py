class Solution(object):
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def findUniquePermutations(self, arr, index, ans):
        if index == len(arr):
            ds = [];
            for i in range(len(arr)):
                ds.append(arr[i]);
            ans.append(list(ds));
            return;
        else:
            seen = set();
            for i in range(index, len(arr)):
                if arr[i] in seen:
                    continue;

                seen.add(arr[i]);
                self.swap(arr, index, i);
                self.findUniquePermutations(arr, index+1, ans);
                self.swap(arr, index, i);
                
                

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        index  = 0;
        nums.sort();
        self.findUniquePermutations(nums, index, ans);
        return ans;
        