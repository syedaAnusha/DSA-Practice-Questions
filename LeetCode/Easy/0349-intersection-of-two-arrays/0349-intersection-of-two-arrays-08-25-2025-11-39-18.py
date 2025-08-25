class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n+m)
    # e.g n = [1,2,3,4] m = [1,2,3,4]
    # Space Complexity: O(n+m) -> just to return the result
    # Auxiliary Complexity: O(n) -> to use it.

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = [];
        uniqueSet = set();
        for i in range(len(nums1)):
            uniqueSet.add(nums1[i]);
        
        for j in range(len(nums2)):
            if nums2[j] in uniqueSet:
                intersection.append(nums2[j]);
                uniqueSet.remove(nums2[j]);
            if not uniqueSet:
                break;
        return intersection;
            

