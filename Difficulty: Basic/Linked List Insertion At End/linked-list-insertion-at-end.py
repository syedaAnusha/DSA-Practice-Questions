'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        temp = head;
        newNode = Node(x);
        
        if temp == None or temp.next == None:
            return newNode;
        
        while temp.next.next != None:
            temp = temp.next;
        
        temp.next.next = newNode;
        return head;
        
        
        