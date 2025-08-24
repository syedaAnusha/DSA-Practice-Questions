class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)+ O(n) -> for temp[] and dupNums[] respectively.


    # check if array is sorted and rotated
    def checkArray(self, arrayA, arrayB, lenArray):
        x = 0;
        i = 0;
        flag = False;
        while i < lenArray and x < lenArray:
            if arrayB[i] == arrayA[(i+x) % lenArray]:
                i += 1;
                flag = True;
            else:
                x += 1;
                i = 0;
                flag = False;
        if flag:
            return True;
        return False;

    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupNums = sorted(nums[::]);
        return self.checkArray(nums, dupNums, len(nums));
        