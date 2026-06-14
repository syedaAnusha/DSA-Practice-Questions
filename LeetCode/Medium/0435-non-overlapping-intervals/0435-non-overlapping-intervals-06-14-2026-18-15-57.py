class Solution:
    # Better Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)
    def sortArrOfIntervals(self, arr):
        arr.sort(key=lambda x:x[1])
        return arr

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = self.sortArrOfIntervals(intervals)
        validIntervals = 1
        endTime = sortedIntervals[0][1]
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] >= endTime:
                endTime = sortedIntervals[i][1];
                validIntervals += 1
        minNumOfIntervals = len(sortedIntervals) - validIntervals 
        return minNumOfIntervals