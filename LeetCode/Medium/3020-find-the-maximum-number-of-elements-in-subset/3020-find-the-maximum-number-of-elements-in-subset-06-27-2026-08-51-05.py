from collections import Counter
class Solution:
    # Optimal Approach
    # Time Complexity: O(n log log M)
    # Space Complexity: O(n)
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        oneCnt = cnt.get(1,0)
        ans = oneCnt if oneCnt % 2 else oneCnt-1
        cnt.pop(1, None)

        for num in cnt:
            res = 0
            x = num
            while x in cnt and cnt[x] > 1:
                res += 2
                x *= x

            if x in cnt:
                ans = max(ans, res+1)
            else:
                ans = max(ans, res-1)
        return ans        