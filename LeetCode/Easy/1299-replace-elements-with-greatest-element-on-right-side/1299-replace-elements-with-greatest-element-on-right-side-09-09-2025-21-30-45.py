class Solution(object):
    # Optimal Solution
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        cur = -1;
        maxNum = float('-inf');
        i = len(arr)-1;
        while i >= 0:
            maxNum = max(cur, maxNum);
            cur = arr[i];
            arr[i] = maxNum;
            i -= 1;  
        return arr;