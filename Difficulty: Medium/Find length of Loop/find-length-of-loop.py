'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLoop(self, head):
        #code here
        if head == None or head.next == None:
            return 0;
        
        hashMap = {};
        temp = head;
        timer = 0;
        cntNodes = 0;
        
        while temp != None:
            timer += 1;
            if temp in hashMap:
                cntNodes = timer - hashMap[temp];
                return cntNodes;
            hashMap[temp] = timer;
            temp = temp.next;
        
        return cntNodes;