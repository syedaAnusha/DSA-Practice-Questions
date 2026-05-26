class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(2 * 2n)
    # Space Complexity: O(1)
    def findAllSubArrays(self, nums, k):
        cntSubArrays = 0;
        left = right = 0;
        oddCnt = 0;
        lenOfNums = len(nums);
        if k < 0:
            return 0;
        while right < lenOfNums:
            if nums[right] & 1:
                oddCnt += 1;
            while oddCnt > k:
                if nums[left] & 1:
                    oddCnt -= 1;   
                left += 1;
            if oddCnt <= k:
                cntSubArrays += (right-left+1);
            right += 1;
        return cntSubArrays;
             
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt1 = self.findAllSubArrays(nums, k);
        cnt2 = self.findAllSubArrays(nums, k-1);
        res = cnt1-cnt2;
        return res;