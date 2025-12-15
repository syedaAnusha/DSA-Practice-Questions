"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self, head):
        # code here
        tempArr = [];
        
        if head == None or head.next == None:
            return head;
        
        temp = head;
        while temp != None:
            tempArr.append(temp.data);
            temp = temp.next;
        
        temp = head;
        while temp != None:
            temp.data = tempArr.pop();
            temp = temp.next;
        
        return head;