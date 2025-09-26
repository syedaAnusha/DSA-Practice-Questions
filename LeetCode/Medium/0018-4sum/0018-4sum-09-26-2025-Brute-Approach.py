class Solution:
    # Brute Force Approach
    # Time Complexity:O(n^4)
    # Space Complexity: 2 * O(list of unique quadruplets) 
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = [];
        tempSet = set();
        n = len(nums);
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        Sum = nums[i] + nums[j] + nums[k] + nums[l];
                        if Sum == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]];
                            temp.sort();
                            tempSet.add(tuple(temp));
        for arr in tempSet:
            ans.append(list(arr));
        return ans;
