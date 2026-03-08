class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n) // just to return ans
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0];
        ans = [0,1];
        if n == 1:
            return ans;
        for i in range(2, n+1):
            if i & 1:
                ans.append(ans[i//2] + 1);
            else:
                ans.append(ans[i//2]);
        return ans;