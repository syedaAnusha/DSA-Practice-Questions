class Solution:
    # Optimal Approach
    # Time Complexity: O(log min(n,m))
    # Space Complexity: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1);
        n2 = len(nums2);
        # we always want our n1 as small array, so we swap
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1);
        low = 0;
        high = n1;
        left = (n1 + n2 + 1) // 2;
        n = n1 + n2; 
        while low <= high:
            mid1 = (low + high) // 2;
            mid2 = left - mid1;
            l1 = float('-inf');
            l2 = float('-inf');
            r1 = float('inf');
            r2 = float('inf');
            if mid1 < n1:
                r1 = nums1[mid1];
            if mid2 < n2:
                r2 = nums2[mid2];
            if mid1-1 >= 0:
                l1 = nums1[mid1-1];
            if mid2-1 >= 0:
                l2 = nums2[mid2-1];
            if l1 <= r2 and l2 <= r1:
                if n%2 == 1:
                    return max(l1, l2);
                median = max(l1, l2) + min(r1, r2);
                return  median / 2;
            elif l1 > r2:
                high =  mid1 - 1;
            else:
                low = mid1 + 1;



        