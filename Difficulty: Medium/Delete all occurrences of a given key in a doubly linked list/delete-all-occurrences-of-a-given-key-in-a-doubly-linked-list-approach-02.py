#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    # Optimal Approach - 2
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeHead(self, temp):
        temp = temp.next;
        temp.prev = None;
        return temp;
        
    def removeTail(self, node):
        temp = node;
        temp.prev.next = None;
        temp = temp.next;
        return temp;
    
    def removeNode(self, node):
        temp = node;
        temp.prev.next = temp.next;
        temp.next.prev = temp.prev;
        temp = temp.next;
        return temp;
        
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        if head == None or (head.next == None and head.data == x):
            return None;
        
        temp = head;
        while temp != None:
            if temp == head and temp.data == x:
                temp = self.removeHead(temp);
                head = temp;
            elif temp.next == None and temp.data == x:
                temp = self.removeTail(temp);
                
            elif temp.data == x:
                temp = self.removeNode(temp);
                
            else:
                temp = temp.next;
        
        return head;
        
        
