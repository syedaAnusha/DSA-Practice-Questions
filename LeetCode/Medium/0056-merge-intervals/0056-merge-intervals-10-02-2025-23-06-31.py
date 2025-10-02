class Solution:
    # Optimal Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [];
        n = len(intervals);
        sortedIntervals = sorted(intervals, key=lambda x:x[0]);
        for i in range(n):
            if len(ans) == 0 or sortedIntervals[i][0] > ans[-1][1]:
                ans.append(sortedIntervals[i]);
            else:
                ans[-1][1] = max(sortedIntervals[i][1], ans[-1][1]);
                 
        return ans;
        