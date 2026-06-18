class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + o(n log n)
    # Space Complexity: O(2n)
    def sortBySingleItem(self, val, wt):
        arr = []
        for i in range(len(val)):
            tple = (val[i], wt[i])
            arr.append(tple)
        arr.sort(key=lambda x:(x[0]/x[1]), reverse=True)
        return arr
        
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        arr = self.sortBySingleItem(val, wt)
        curWeight = 0
        totalValue = 0.0
        
        for i in range(len(arr)):
            if curWeight + arr[i][1] <= capacity:
                totalValue += arr[i][0]
                curWeight += arr[i][1]
            else:
                remainWt = capacity - curWeight
                reqVal = (arr[i][0] / arr[i][1]) * remainWt
                totalValue += reqVal
                break
                
        return totalValue
        