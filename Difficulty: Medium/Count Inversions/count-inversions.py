class Solution:
    def mergeSort(self, arr, low, mid, high):
        temp = []
        i = low
        j = mid + 1
        invCount = 0

        # Merge step
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                invCount += (mid - i + 1)  # count inversions
                j += 1

        # Copy remaining elements
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1

        # Copy back into arr
        for k in range(low, high + 1):
            arr[k] = temp[k - low]

        return invCount

    def findInversionCounts(self, arr, low, high):
        count = 0
        if low < high:
            mid = (low + high) // 2
            count += self.findInversionCounts(arr, low, mid)
            count += self.findInversionCounts(arr, mid + 1, high)
            count += self.mergeSort(arr, low, mid, high)
        return count

    def inversionCount(self, arr):
        return self.findInversionCounts(arr, 0, len(arr) - 1)
