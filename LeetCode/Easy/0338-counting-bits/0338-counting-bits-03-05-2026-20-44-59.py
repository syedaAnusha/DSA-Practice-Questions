class Solution:
    # Better Approach
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    def getCountSetBits(self, n):
        cnt = 0;
        while n > 0:
            n = n & (n-1);
            cnt  += 1;
        return cnt;

    def countBits(self, n: int) -> List[int]:
        ans = [];
        for i in range(0, n+1):
            cnt = self.getCountSetBits(i);
            ans.append(cnt);
        return ans;