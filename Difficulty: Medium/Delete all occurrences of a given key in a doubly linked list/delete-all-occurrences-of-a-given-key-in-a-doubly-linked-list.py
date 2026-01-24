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
    def deleteAllOccurOfX(self, head, x):
        # code here
        
            
        temp = head;
        while temp != None:
            if temp.data == x:
                if temp == head:
                    head = head.next;
                prevNode = temp.prev;
                nextNode = temp.next;
                if prevNode:
                    prevNode.next = nextNode;
                if nextNode:
                    nextNode.prev = prevNode;
                
                temp = nextNode;
            else:
                temp = temp.next;
        return head;