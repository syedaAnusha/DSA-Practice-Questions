class Solution(object):
    def findCombinationSum3(self, arr, k, n, ds, ans, index):
        if  n == 0 and k == 0:
            ans.append(list(ds));
            return;
        for i in range(index, len(arr)):
            if arr[i] > n:
                break;
            ds.append(arr[i]);
            self.findCombinationSum3(arr, k-1, n - arr[i], ds, ans, i+1);
            ds.remove(arr[i]);
       
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """  
        # since we can use only distinct numbers from 1 to 9
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        ds  = [];
        ans = [];
        self.findCombinationSum3(arr, k, n, ds, ans, 0);
        return ans;
        