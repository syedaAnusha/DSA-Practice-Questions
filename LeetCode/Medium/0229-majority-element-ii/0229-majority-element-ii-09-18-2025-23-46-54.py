class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n) = O(2n) = O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [];
        cnt1 = 0;
        cnt2 = 0;
        elem1 = float('-inf');
        elem2 = float('-inf');

        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != elem2:
                cnt1 = 1;
                elem1 = nums[i];
            elif cnt2 == 0 and nums[i] != elem1:
                cnt2 = 1;
                elem2 = nums[i];
            elif nums[i] == elem1:
                cnt1 += 1;
            elif nums[i] == elem2:
                cnt2 += 1;
            else:
                cnt1 -= 1;
                cnt2 -= 1;

        cnt1 = 0;
        cnt2 = 0;
        minNum = (len(nums) // 3);
        for j in range(len(nums)):
            if nums[j] == elem1:
                cnt1 += 1;
            elif nums[j] == elem2:
                cnt2 += 1;
        
        if cnt1 > minNum:
            ans.append(elem1);
        if cnt2 > minNum:
            ans.append(elem2);

        return ans;

        