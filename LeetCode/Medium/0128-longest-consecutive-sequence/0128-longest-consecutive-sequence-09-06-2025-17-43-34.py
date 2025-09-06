class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n) + O(2n) = O(3n) = O(n) 
    # Space Complexity: O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0;
        cnt = 0;
        hashSet = set(nums); # unorderedset takes O(1) time in search 
        for num in hashSet:
            if num-1 not in hashSet:
                cnt += 1;
                elem = num+1;
                while elem in hashSet:
                    cnt += 1;
                    elem += 1;   
                longest = max(longest, cnt);
                cnt = 0;
        return longest;


        