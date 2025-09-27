import math;
class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(log(n+m)) * O(n+m)
    # Space Complexity: O(1)
    def swap(self, nums1, nums2, i, j):
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i];
        
    def mergeArrays(self, a, b):
        # code here
        length = len(a) + len(b);
        gap = math.ceil((len(a) + len(b)) / 2);
        while gap > 0:
            left = 0;
            right = left + gap;
            while right < length:
                # if left is in a and right is in b
                if left < len(a) and right >= len(a):
                    self.swap(a, b, left, right-len(a));
                # if left and right are in b
                elif left >= len(a):
                    self.swap(b, b, left-len(a), right-len(a));
                # if left and right are in a
                else:
                    self.swap(a, a, left, right);
                left += 1;
                right += 1;
            if gap == 1:
                break;
            else:
                gap = math.ceil(gap/2);
