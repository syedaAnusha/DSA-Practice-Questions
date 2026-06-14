class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(nlogn) + O(n) + O(nlogn)
    # Space Complexity: O(n) + O(n)
    def getAndSortArrOfTuple(self, s, f):
        S = len(s)
        arr = []
        for i in range(S):
            tple = (i, s[i], f[i])
            arr.append(tple)
        arr.sort(key=lambda x:x[2])
        return arr
        
    def maxMeetings(self, s: list[int], f: list[int]) -> list[int]:
        # code here
        arr = self.getAndSortArrOfTuple(s, f)
        sT = float("-inf")
        eT = float("-inf")
        lenOfArr = len(arr)
        ans = []
        for i in range(lenOfArr):
            startTime = arr[i][1]
            endTime = arr[i][2]
            if eT < startTime:
                ans.append(arr[i][0]+1)
                eT = endTime
        ans.sort()
        return ans