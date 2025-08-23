class Solution(object):
    # Optimal Approach
    # Time Complexity: O(D) + O(N) - O(D) + O(D)  ≈ O(N) + O(D) ≈ O(N+D)
    # Space Complexity: O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def reverseArray(self, arr, i, j):
        while i <= j:
            self.swap(arr, i, j);
            i += 1;
            j -= 1;
            
    def rightRotation(self, arr, k):
        n = len(arr);
        k = k % n;
        kthIndex = n-k;

        # Reverse K elements of an array
        self.reverseArray(arr, kthIndex, n-1);
        
        # Reverse non-k elements of an array
        self.reverseArray(arr, 0, kthIndex-1);

        # Reverse entire array
        self.reverseArray(arr, 0, n-1);


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.rightRotation(nums, k);


        