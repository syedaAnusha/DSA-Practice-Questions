#User function Template for python3
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(n)
    def rearrange(self,arr):
        # code here
        pos = [];
        neg = [];
        for i in range(len(arr)):
            if arr[i] < 0:
                neg.append(arr[i]);
            else:
                pos.append(arr[i]);
        
        if len(pos) > len(neg):
            for j in range(len(neg)):
                arr[2*j] = pos[j];
                arr[(2*j)+1] = neg[j];
                
            index = len(neg)*2;
            for k in range(len(neg), len(pos)):
                arr[index] = pos[k];
                index += 1;
        else:
            for j in range(len(pos)):
                arr[2*j] = pos[j];
                arr[(2*j)+1] = neg[j];
                
            index = len(pos)*2;
            for k in range(len(pos), len(neg)):
                arr[index] = neg[k];
                index += 1;
        
            
                
            
            
