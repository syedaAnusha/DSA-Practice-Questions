"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        # edge cases
        if head == None or (x == 1 and head.next == None):
            return None;
        
        temp = head;
        if x == 1:
            temp = temp.next;
            temp.prev = None;
            head.next = None;
            return temp;
        
        countNodes = 1;
        while temp != None:
            if countNodes == x:
                temp.prev.next = temp.next;
                if temp.next != None:
                    temp.next.prev = temp.prev
                else:
                    temp.prev = None;
                break;
            temp = temp.next;
            countNodes += 1;
        
        return head;
            
            
            
        
        
        