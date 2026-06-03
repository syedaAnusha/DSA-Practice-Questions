Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.



A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.

A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.

Examples:
Input: nums = [10, 20, 30, 21, 23]

Output: [30, 21, 23, 10, 20]

Explanation:

Input: nums = [-5, -4, -3, -2, -1]

Output: [-1, -2, -3, -4, -5]

Explanation:

Input: nums = [2, 6, 3, 100, 120, 4, 5]

Constraints
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums represents a min-heap
