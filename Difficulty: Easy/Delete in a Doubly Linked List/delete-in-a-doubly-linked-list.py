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
        if head == None:
            return None;
            
        countNode = 0;
        temp = head;
        while temp != None:
            countNode += 1;
            if countNode == x:
                break;
            temp = temp.next;
        
        prevNode = temp.prev;
        nextNode = temp.next;
        
        if prevNode == None and nextNode == None:
            return None;
        elif nextNode == None:
            prevNode.next = None;
            temp.prev = None;
            return head;
        elif prevNode == None:
            temp = nextNode;
            temp.prev = None;
            return temp;
        else:
            prevNode.next = nextNode;
            nextNode.prev = prevNode;
            temp.next = None;
            temp.prev = None;
            return head;
            
            