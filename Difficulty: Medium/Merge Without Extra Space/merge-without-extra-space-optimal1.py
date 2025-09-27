class Solution:
    # Brute Force Approach
    # Time Complexity: O(min(a,b)) + O(nlogn) + O(mlogm)
    # Space Complexity: O(1)
    def swap(self, nums1, nums2, i, j):
        nums1[i], nums2[j] = nums2[j], nums1[i];
        
    def mergeArrays(self, a, b):
        # code here
        left = len(a)-1;
        right = 0;
        while left >= 0 and right < len(b):
            if a[left] > b[right]:
                self.swap(a, b, left, right);
                left -= 1;
                right += 1;
            else:
                break;
                
        a.sort();
        b.sort();
