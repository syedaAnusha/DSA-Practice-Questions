class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [];
        for i in range(len(nums)):
            if len(ans) == 0 or ans[-1] != nums[i]:
                cnt = 0;
                for j in range(len(nums)):
                    if nums[i] == nums[j]:
                        cnt += 1;
                if cnt > (len(nums) // 3):
                    ans.append(nums[i]);
            if len(ans) == 2:
                break;
        return ans;
