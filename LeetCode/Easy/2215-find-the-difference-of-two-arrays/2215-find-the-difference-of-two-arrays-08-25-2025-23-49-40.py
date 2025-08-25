class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(2(n1*n2)) + O(n1+n2) ≈ O(n1∗n2)
    # Space Complexity: O(n1) + O(n2) -> for returning the result
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1 = set(nums1);
        n2 = set(nums2);
        res1 = [];
        res2 = [];

        for num1 in n1:
            if num1 not in n2:
                res1.append(num1);
        
        for num2 in n2:
            if num2 not in n1:
                res2.append(num2);
        
        return [res1, res2];



        