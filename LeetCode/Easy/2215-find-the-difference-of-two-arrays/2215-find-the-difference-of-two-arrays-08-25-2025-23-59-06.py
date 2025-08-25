class Solution(object):
    # Optimal Approach 2
    # Time Complexity: O(n1 + n2) +  O(n1 + n2) ≈ O(2(n1+n2)) ≈ O(n1+n2) 
    # Space Complexity: O(n1) + O(n2) -> for returning the result
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1 = set(nums1);
        n2 = set(nums2);

        res1 = n1 - n2;
        res2 = n2 - n1;
        
        return [list(res1), list(res2)];



        