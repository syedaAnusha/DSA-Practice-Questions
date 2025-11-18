class Solution:
    # Optimal Solution
    # Time Complexity: O(n) * O(2^n)
    # Space Complexity: O(n) * O(2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        n = len(nums);
        subsets = 1 << n;
        for num in range(subsets):
            tempLst = [];
            for i in range(len(nums)):
                if num & (1 << i):
                    tempLst.append(nums[i]);
            ans.append(tempLst);
        return ans;

        