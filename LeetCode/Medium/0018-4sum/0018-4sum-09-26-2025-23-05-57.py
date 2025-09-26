class Solution:
    # Better Approach
    # Time Complexity:O(n^3 + O(log m))
    # Space Complexity: O(n) +  2 * O(list of unique quadruplets) 
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = [];
        tempSet = set();
        n = len(nums);
        for i in range(n):
            for j in range(i+1, n):
                hashSet = set();
                for k in range(j+1, n):
                    fourthElem = target - (nums[i] + nums[j] + nums[k]);
                    if fourthElem in hashSet:
                        temp = [nums[i], nums[j], nums[k], fourthElem];
                        temp.sort();
                        tempSet.add(tuple(temp));
                    hashSet.add(nums[k]);
                    
        for arr in tempSet:
            ans.append(list(arr));
        return ans;
