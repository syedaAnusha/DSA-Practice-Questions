class Solution:
    # Better Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        N = len(intervals)
        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < N and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        while i < N:
            res.append(intervals[i])
            i += 1
        return res