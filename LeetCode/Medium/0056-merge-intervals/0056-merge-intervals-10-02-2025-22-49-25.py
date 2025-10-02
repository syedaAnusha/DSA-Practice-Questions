class Solution:
    # Brute Force Approach
    # Time Complexity: O(nlogn) + O(2n)
    # Space Complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [];
        n = len(intervals);
        sortedIntervals = sorted(intervals, key=lambda x:x[0]);
        for i in range(n):
            start = sortedIntervals[i][0];
            end = sortedIntervals[i][1];
            if len(ans) != 0 and end <= ans[-1][1]:
                continue;
            for j in range(i+1, n):
                if sortedIntervals[j][0] <= end:
                    end = max(sortedIntervals[j][1], end);
                else:
                    break;
            ans.append([start, end]);
        return ans;
        