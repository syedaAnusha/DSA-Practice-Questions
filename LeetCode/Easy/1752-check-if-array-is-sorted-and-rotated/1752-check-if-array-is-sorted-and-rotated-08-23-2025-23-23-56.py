class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)+ O(n) -> for temp[] and dupNums[] respectively.
    
    # Sort duplicate array
    def mergeArray(self, arr, low, mid, high):
        i = low;
        j = mid + 1;
        temp = [];
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i]);
                i += 1;
            else:
                temp.append(arr[j]);
                j += 1;
        if i <= mid:
            while i <= mid:
                temp.append(arr[i]);
                i += 1;
        else:
            while j <= high:
                temp.append(arr[j]);
                j += 1;

        for index in range(len(temp)):
            arr[low+index] = temp[index];


    def sortArray(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2;
            self.sortArray(arr, low, mid);
            self.sortArray(arr, mid+1, high);
            self.mergeArray(arr, low, mid, high);

    # check if array is sorted and rotated
    def checkArray(self, arrayA, arrayB, lenArray):
        x = 0;
        i = 0;
        flag = False;
        while i < lenArray and x < lenArray:
            if arrayB[i] == arrayA[(i+x) % lenArray]:
                i += 1;
                flag = True;
            else:
                x += 1;
                i = 0;
                flag = False;
        if flag:
            return True;
        return False;

    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupNums = nums[::];
        self.sortArray(dupNums, 0, len(nums)-1);
        return self.checkArray(nums, dupNums, len(nums));
        
