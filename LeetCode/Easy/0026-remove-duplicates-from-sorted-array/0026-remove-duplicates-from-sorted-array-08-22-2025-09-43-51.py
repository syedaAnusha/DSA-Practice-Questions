class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(1) + O(logn) + O(n) = O(n+logn)
        # Space Complexity: O(n) +  O(n);
        uniqueSet = set();
        for i in range(len(nums)):
            uniqueSet.add(nums[i]);

        sortedUniqueLst = sorted(list(uniqueSet));
        index = 0;
        for elem in sortedUniqueLst:
            nums.insert(index, elem);
            index += 1;
        
        return index;



        