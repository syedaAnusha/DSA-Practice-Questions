"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self, head):
        # code here
        
        if head == None or head.next == None:
            return head;
        
        currNode = head;
        while currNode != None:
            prevNode = currNode.prev;
            currNode.prev = currNode.next
            currNode.next = prevNode;
            currNode = currNode.prev;
        return prevNode.prev;
