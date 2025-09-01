class Solution(object):
    # Optimal Approach - Moore's Voting Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0;
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1;
                elem = nums[i];
            elif nums[i] == elem:
                cnt += 1;
            else:
                cnt -= 1;
        return elem;
                

            

