class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n*n) =>  O(n^2)
    # Space Complexity: O(n) + O(n) => O(2n) = O(n) 

    def findnCr(self, n, r):
        res = 1;
        for i in range(r):
            res = res * (n-i);
            res = res // (i+1);
        return res;

    def generateRow(self, row):
        ans = 1;
        ansRow = [];
        ansRow.append(1);
        for col in range(1, row):
            ans = ans * (row-col);
            ans = ans // col;
            ansRow.append(ans);
        return ansRow;

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [];
        for r in range(1, numRows+1):
            ans.append(self.generateRow(r));
        return ans;
        