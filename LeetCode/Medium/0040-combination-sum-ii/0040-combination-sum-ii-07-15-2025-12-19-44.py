class Solution(object):
    def findCombinationSum2(self, arr, index, target, ds, ans):
        if target == 0:
            ans.append(list(ds));
            return;
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i-1]:
                continue;
            if arr[i] > target:
                break;
            ds.append(arr[i]);
            self.findCombinationSum2(arr, i+1, target-arr[i], ds, ans);
            ds.remove(arr[i]);

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort();
        ans = [];
        self.findCombinationSum2(candidates,0, target, [], ans);
        return ans;
        