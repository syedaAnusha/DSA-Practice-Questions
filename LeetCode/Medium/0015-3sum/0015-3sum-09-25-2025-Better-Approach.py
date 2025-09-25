class Solution:
    # Better Approach
    # Time Complexity: O(n^2 * log(size of hashset))
    # Space Complexity: O(n) +  2 * O(no: of unique triplets)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        n = len(nums);
        tempSet = set();

        for i in range(n):
            hashSet = set();
            for j in range(i+1, n):
                thirdElem = -(nums[i] + nums[j]);
                if thirdElem in hashSet:
                    temp = [nums[i], nums[j], thirdElem];
                    temp.sort();
                    tempSet.add(tuple(temp));
                hashSet.add(nums[j]);
                                     
        for item in tempSet:
            ans.append(list(item));

        return ans;
