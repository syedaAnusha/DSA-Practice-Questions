class Solution:
    # Better Approach
    # Time Complexity: O(2 n log n) + O(arr + dep)
    # Space Complexity: O(1)

    def minPlatform(self, arr, dep):
        # code here
        if len(arr) == 0:
            return 1
        arr.sort()
        dep.sort()
        i = j = 0
        cnt = 0
        maxPlatformCnt = 0
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            maxPlatformCnt = max(maxPlatformCnt, cnt)
        return maxPlatformCnt