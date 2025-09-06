class Solution(object):
    # Better Approach
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1) -> if distorting an original arr
    # Space Complexity: O(n) -> if creating a duplicate copy of arr.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0;
        lastSmaller = float('-inf');
        sortedList = sorted(nums);
        cnt = 0;
        for i in range(len(sortedList)):
            if sortedList[i]-1 == lastSmaller:
                lastSmaller = sortedList[i];
                cnt += 1;
            elif lastSmaller != sortedList[i]:
                lastSmaller = sortedList[i];
                cnt = 1;
            longest = max(longest, cnt);

        return longest;


        