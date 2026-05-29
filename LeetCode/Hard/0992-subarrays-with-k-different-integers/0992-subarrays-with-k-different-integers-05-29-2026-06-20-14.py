class Solution:
    # Optimal Approach
    # Time Complexity: O(2 * 2n)
    # Space Complexity: O(k)
    def findAllSubarrays(self, nums, k):
        left = right = 0;
        N = len(nums);
        hashMap = {};
        cntSubArrays = 0;

        if k < 0:
            return 0;
        while right < N:
            if nums[right] in hashMap:
                hashMap[nums[right]] += 1;
            else:
                hashMap[nums[right]] = 1;
            while len(hashMap) > k:
                hashMap[nums[left]] -= 1;
                if hashMap[nums[left]] == 0:
                    hashMap.pop(nums[left]);
                left += 1;
            if len(hashMap) <= k:
                cntSubArrays += (right-left+1);
            right += 1;
        return cntSubArrays;

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt1 = self.findAllSubarrays(nums, k);
        cnt2 = self.findAllSubarrays(nums, k-1);
        ans = cnt1-cnt2;
        return ans;
        