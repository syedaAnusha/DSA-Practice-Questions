class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Optimal Solution
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def solve(self, A):
        ans = [];
        i = len(A)-2;
        maxNum = A[len(A)-1];
        ans = [maxNum];
        while i >= 0:
            if A[i] > maxNum:
                ans.append(A[i]);
                maxNum = A[i];
            i -= 1;
        return ans;
