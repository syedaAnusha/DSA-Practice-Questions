'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n log n) + O(n)
    # Space Complexity: O(n)
    def segregate(self, head):
        #code here
        if head == None or head.next == None:
            return head;
        temp = head;
        tempArr = [];
        while temp != None:
            tempArr.append(temp.data);
            temp = temp.next;
        
        tempArr.sort();
        temp = head;
        for i in range(len(tempArr)):
            temp.data = tempArr[i];
            temp = temp.next;
        return head;
        
    