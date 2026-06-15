class Solution:
    # Optimal Approach - 02 (Greedy)
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(2n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        ans = []
        n = len(intervals)
        sortedIntervals = sorted(intervals)
        start = sortedIntervals[0][0]
        end = sortedIntervals[0][1]
        i = 1
        while i < n:
            while i < n and end < sortedIntervals[i][0]:
                ans.append([start, end])
                start = sortedIntervals[i][0]
                end = sortedIntervals[i][1]
                i += 1

            while i < n and end >= sortedIntervals[i][0]:
                start = min(start, sortedIntervals[i][0])
                end = max(end, sortedIntervals[i][1])
                print(start, end)
                i += 1
            ans.append([start, end])
            if i < n:
                start = sortedIntervals[i][0]
                end = sortedIntervals[i][1]
        return ans