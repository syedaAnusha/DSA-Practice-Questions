class Solution:
    # Optimal Approach
    # Time Complexity: O(n log n) +  O(n * n)
    # Space Complexity: O(no: of unique triplets)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        n = len(nums);
        nums.sort();
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue;
            j = i + 1;
            k = n-1;
            while j < k:
                Sum = nums[i] + nums[j] + nums[k];
                if Sum < 0:
                    j += 1;
                
                elif Sum > 0:
                    k -= 1;
                
                else:
                    temp = [nums[i], nums[j], nums[k]];
                    ans.append(temp);
                    j += 1;
                    k -= 1;
                    while j < k and nums[j] == nums[j-1]:
                        j += 1;
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1;
        return ans;


        