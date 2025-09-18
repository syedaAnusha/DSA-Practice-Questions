class Solution:
    # Better Approach - II
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [];
        majorityCountSet = {};
        minNum = (len(nums) // 3) + 1;
        for i in range(len(nums)):
            if nums[i] in majorityCountSet:
                majorityCountSet[nums[i]] += 1;
            else:
                majorityCountSet[nums[i]] = 1;

            if majorityCountSet[nums[i]] == minNum:
                ans.append(nums[i]);

        return ans;

        