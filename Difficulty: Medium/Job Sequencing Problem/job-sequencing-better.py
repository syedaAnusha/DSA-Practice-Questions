class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(n log n) + O(n*d)
    # Space Complexity: O(n) + O(d)
    # Optimal Approach is, where we use disjoint union concept : later in graphs section.
    def jobSequencing(self, deadline, profit):
        # code here
        arr = []
        maxProfit = 0
        maxNumOfJobs = 0
        for i in range(len(deadline)):
            jobTuple = (i, deadline[i], profit[i])
            arr.append(jobTuple)
        arr.sort(key=lambda x:x[2], reverse=True)
        maxDeadline = float("-inf")
        for i in range(len(arr)):
            maxDeadline = max(maxDeadline, arr[i][1])
        slots = [-1] * (maxDeadline+1)
        N = len(arr)

        for i in range(N):
            for j in range(arr[i][1], 0, -1):
                if slots[j] == -1:
                    slots[j] = arr[i][0]
                    maxProfit += arr[i][2]
                    maxNumOfJobs += 1
                    break
        return [maxNumOfJobs, maxProfit]
