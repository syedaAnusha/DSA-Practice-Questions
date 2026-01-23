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
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        if head == None or (head.next == None and head.data == x):
            return None;
        
        temp = head;
        while temp != None:
            if temp == head and temp.data == x:
                temp = temp.next;
                temp.prev = None;
                head = temp;
            elif temp.next == None and temp.data == x:
                temp.prev.next = None;
                temp = temp.next;
            elif temp.data == x:
                temp.prev.next = temp.next;
                temp.next.prev = temp.prev;
                temp = temp.next;
            else:
                temp = temp.next;
        
        return head;