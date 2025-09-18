class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(len(majorityCountSet))
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [];
        majorityCountSet = {};
        for i in range(len(nums)):
            if nums[i] in majorityCountSet:
                majorityCountSet[nums[i]] += 1;
            else:
                majorityCountSet[nums[i]] = 1;

        for key, value in majorityCountSet.items():
            if value > (len(nums)//3):
                ans.append(key);

        return ans;

        