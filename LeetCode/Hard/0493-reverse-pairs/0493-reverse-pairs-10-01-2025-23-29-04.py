class Solution:
    # Optimal Approach
    # Time Complexity: 2*n + O(logn)
    # Space Complexity: O(n)
    def countPairs(self, nums, low, mid, high):
        j = mid+1;
        pairsCounter = 0;
        for i in range(low, mid+1):
            while j <= high and nums[i] > 2*nums[j]:
                j += 1;
            pairsCounter += (j-(mid+1));  
        return pairsCounter;    

    def mergePairs(self, nums, low, mid, high):
        i = low;
        j = mid+1;
        temp = [];
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i]);
                i += 1;
            else:
                temp.append(nums[j]);
                j += 1;

        while i <= mid:
            temp.append(nums[i]);
            i += 1;
        
        while j <= high:
            temp.append(nums[j]);
            j += 1;

        # sorting original array
        for index in range(low, high+1):
            nums[index] = temp[index-low];
        return nums;

    def mergeSort(self, nums, low, high):
        pairsCounter = 0;
        if low < high:
            mid = (low + high) // 2;
            pairsCounter += self.mergeSort(nums, low, mid);
            pairsCounter += self.mergeSort(nums, mid+1, high);
            pairsCounter += self.countPairs(nums, low, mid, high);
            self.mergePairs(nums, low, mid, high);
        return pairsCounter;

    def reversePairs(self, nums: List[int]) -> int:
        low = 0;
        high = len(nums)-1;
        return self.mergeSort(nums, low, high);
        