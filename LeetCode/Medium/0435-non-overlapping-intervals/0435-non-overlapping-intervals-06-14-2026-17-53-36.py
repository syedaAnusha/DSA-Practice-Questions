class Solution:
    # Better Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)
    def sortArrOfIntervals(self, arr):
        arr.sort(key=lambda x:x[1])
        return arr

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = self.sortArrOfIntervals(intervals)
        print("arr", sortedIntervals)
        minNumOfIntervals = 0
        end = sortedIntervals[0][1]
        for i in range(1, len(sortedIntervals)):
            if end != sortedIntervals[i][0] and end > sortedIntervals[i][0]:
                minNumOfIntervals += 1;
            else:
                end = sortedIntervals[i][1]
        return minNumOfIntervals