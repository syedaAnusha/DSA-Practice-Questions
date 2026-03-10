
class Solution:
    # Approach 01
    # Time Complexity: O(n*q)
    # Space Complexity: O(q)
    def count_NGE(self, arr, indices):
        # Code here
        ans = [];
        for i in range(len(indices)):
            count = 0;
            index = indices[i];
            elem = arr[index];
            for j in range(index+1, len(arr)):
                if arr[j] > elem:
                    count += 1;
            ans.append(count);
        return ans;