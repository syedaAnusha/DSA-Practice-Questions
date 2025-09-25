class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^3 * log(no: of unique triplets))
    # Space Complexity: 2 * O(no: of triplets)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        n = len(nums);
        tempSet = set();

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    Sum = nums[i] + nums[j] + nums[k];
                    if Sum == 0:
                        temp = [nums[i], nums[j], nums[k]];
                        temp.sort();
                        tempSet.add(tuple(temp));
                        
        for item in tempSet:
            ans.append(list(item));

        return ans;
