class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i];

    def convertMinToMaxHeap(self, nums, index, size):
        while True:
            largest = index;
            left = 2*index+1;
            right = 2*index+2;

            if left < size and nums[left] > nums[largest]:
                largest = left;
            if right < size and nums[right] > nums[largest]:
                largest = right;

            if largest != index:
                self.swap(nums, largest, index);
                index = largest;
            else:
                break;

    def minToMaxHeap(self, nums):
        N = len(nums);
        NonLeafNodeIndex = N//2 - 1;
        while NonLeafNodeIndex >= 0:
            self.convertMinToMaxHeap(nums, NonLeafNodeIndex, N);
            NonLeafNodeIndex -= 1;
        return nums;
