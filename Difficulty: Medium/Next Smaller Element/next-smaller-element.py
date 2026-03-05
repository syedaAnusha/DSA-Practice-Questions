class Solution:
    # Optimal Approach
    # Time Complexity: O(n) +  O(n)
    # Space Complexity: O(n) + O(n)
	def nextSmallerEle(self, arr):
		# code here
		ans = [];
		stack = [];
		
		for i in range(len(arr)-1,-1,-1):
		    while stack and arr[i] <= stack[-1]:
		        stack.pop();
		    if not stack:
		        ans.append(-1);
		    else:
		        ans.append(stack[-1]);
		    stack.append(arr[i]);
	    return ans[::-1];