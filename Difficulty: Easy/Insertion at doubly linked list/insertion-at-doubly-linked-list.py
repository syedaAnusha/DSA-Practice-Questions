'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        if head == None:
            return None;
        
        temp = head;
        cntNodes = 0;
        
        while temp.next != None:
            if cntNodes == p:
                break;
            temp = temp.next;
            cntNodes += 1;
        
        newNode = Node(x);
        if temp.next == None:
            temp.next = newNode;
            newNode.prev = temp;
        else:
            prevNode = temp;
            nextNode = temp.next;
            prevNode.next = newNode;
            nextNode.prev = newNode;
            newNode.prev = prevNode;
            newNode.next = nextNode;
        
        return head;
        
        
            
        
        