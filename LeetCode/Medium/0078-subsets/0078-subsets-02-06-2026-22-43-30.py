class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^n)*O(n)
    # Space Complexity: O(k) * O(2^n), where k is an avg length of subset array
    def findAllSubsets(self, index, nums, resArr, tempArr):
        resArr.append(list(tempArr));
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue;
            tempArr.append(nums[i]);
            self.findAllSubsets(i+1, nums, resArr, tempArr);
            tempArr.remove(nums[i]);
        return resArr;


    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [];
        temp = [];
        index = 0;
        return self.findAllSubsets(index, nums, res, temp);