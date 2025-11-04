class Solution:
    # Better Approach
    # Time Complexity: O(n+m)
    # Space Complexity: O(1)
    def findMedian(Self, nums1, nums2):
        i = 0;
        j = 0;
        cnt = 0;
        n = len(nums1) + len(nums2);
        index1 = n // 2;
        index2 = index1 - 1;
        elem1 = float('inf');
        elem2 = float('inf');
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if cnt == index1:
                    elem1 = nums1[i];
                if cnt == index2:
                    elem2 = nums1[i];
                cnt += 1;
                i += 1;
            else:
                if cnt == index1:
                    elem1 = nums2[j];
                if cnt == index2:
                    elem2 = nums2[j];
                cnt += 1;
                j += 1;

        while i < len(nums1):
            if cnt == index1:
                elem1 = nums1[i];
            if cnt == index2:
                elem2 = nums1[i];
            cnt += 1;
            i += 1;

        while j < len(nums2):
            if cnt == index1:
                elem1 = nums2[j];
            if cnt == index2:
                elem2 = nums2[j];
            cnt += 1;
            j += 1;
        
        if n%2 == 1:
            return elem1;

        median = (elem1 + elem2) / 2;
        return median;
         

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedian(nums1, nums2);


        