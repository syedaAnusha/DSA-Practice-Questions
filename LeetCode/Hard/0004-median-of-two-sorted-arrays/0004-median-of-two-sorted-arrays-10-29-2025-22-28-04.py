class Solution:
    # Brute Force Approach
    # Time Complexity: O(n+m)
    # Space Complexity: O(n+m)
    def mergeSortedArrays(Self, nums1, nums2):
        i = 0;
        j = 0;
        temp = [];
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i]);
                i += 1;
            else:
                temp.append(nums2[j]);
                j += 1;
        while i < len(nums1):
            temp.append(nums1[i]);
            i += 1;
        while j < len(nums2):
            temp.append(nums2[j]);
            j += 1;
        return temp;

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2);
        mergedArr = self.mergeSortedArrays(nums1, nums2);
        index = n // 2;
        if n % 2 == 1:
            return mergedArr[index];
        else:
            return (mergedArr[index] + mergedArr[index-1]) / 2;


        