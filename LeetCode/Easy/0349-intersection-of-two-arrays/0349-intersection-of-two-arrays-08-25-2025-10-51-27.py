class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n+m) + O(nlogn) + O(mlogm) = O(nlogn + mlogm)
    # e.g n = [1,2,3,4] m = [1,2,3,4]
    # Space Complexity: O(min(n,m))

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = [];
        i = 0;
        j = 0;
        lenNums1 = len(nums1);
        lenNums2 = len(nums2);
        nums1 = sorted(nums1);
        nums2 = sorted(nums2);
        
        while i < lenNums1 and j < lenNums2:
            if nums1[i] < nums2[j]:
                i += 1;
            elif nums2[j] < nums1[i]:
                j += 1;
            else:
                if len(intersection) == 0 or intersection[-1] != nums1[i]:
                    intersection.append(nums1[i]);
                i += 1; 
        return intersection;
        