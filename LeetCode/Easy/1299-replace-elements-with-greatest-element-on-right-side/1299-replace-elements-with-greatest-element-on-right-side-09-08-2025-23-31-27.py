class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n)*O(n-1) = O(n^2)
    # Space Complexity: O(1)
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)):
            maxNum = float('-inf');
            for j in range(i+1, len(arr)):
                maxNum = max(maxNum, arr[j]);
            if i == len(arr)-1:
                arr[i] = -1;
            else:
                arr[i] = maxNum;
        return arr;
