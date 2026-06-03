class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(k log n)
    # Space Complexity: O(1)
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i];

    def convertToMaxHeap(self, nums, index, size):
        while True:
            smallest = index;
            left = 2*index+1;
            right = 2*index+2;
            if left < size and nums[left] > nums[smallest]:
                smallest = left;
            if right < size and nums[right] > nums[smallest]:
                smallest = right;

            if smallest != index:
                self.swap(nums, smallest, index);
                index = smallest;
            else:
                break;

    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums);
        nonLeafNodeIndex = N//2 - 1;
        count = k;
        while nonLeafNodeIndex >= 0:
            self.convertToMaxHeap(nums, nonLeafNodeIndex, N);
            nonLeafNodeIndex -= 1;
        
        while count > 0:
            KthLargestElement = nums[0];
            nums[0] = nums[N-1];
            N -= 1;
            self.convertToMaxHeap(nums, 0, N);
            count -= 1;
        return KthLargestElement;      