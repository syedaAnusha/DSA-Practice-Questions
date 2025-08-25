class Solution(object):
    # Brute Force Approach
    # Time Complexity: 
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1 = set();
        n2 = set();
        flag = False;
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = True;
                    break;
            if not flag:
                n1.add(nums1[i]);
            else:
                flag = False;

        for j in range(len(nums2)):
            for i in range(len(nums1)):
                if nums2[j] == nums1[i]:
                    flag = True;
                    break;
            if not flag:
                n2.add(nums2[j]);
            else:
                flag = False;

        return [list(n1), list(n2)];