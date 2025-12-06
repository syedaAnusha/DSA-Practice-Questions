'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def removeLastNode(self, head):
        # code here
        temp = head;
        if temp == None or temp.next == None:
            return None;
            
        while temp.next.next != None:
            temp = temp.next;
        temp.next = None;
        return head;
        