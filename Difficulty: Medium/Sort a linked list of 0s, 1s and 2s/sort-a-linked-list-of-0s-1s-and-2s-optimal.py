'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def segregate(self, head):
        #code here
        if head == None or head.next == None:
            return head;
        dummyNodeZero = Node(-1);
        dummyNodeOne = Node(-1);
        dummyNodeTwo = Node(-1);
        moverZero = dummyNodeZero;
        moverOne = dummyNodeOne;
        moverTwo = dummyNodeTwo;
        temp = head;
        
        while temp != None:
            if temp.data == 0:
                moverZero.next = temp;
                moverZero = temp;
            elif temp.data == 1:
                moverOne.next = temp;
                moverOne = temp;
            else:
                moverTwo.next = temp;
                moverTwo = temp;
            temp = temp.next;
        if dummyNodeZero.next:
            if dummyNodeOne.next:
                moverZero.next = dummyNodeOne.next;
            else:
                moverZero.next = dummyNodeTwo.next;
        if dummyNodeOne.next:
                moverOne.next = dummyNodeTwo.next;
        moverTwo.next = None;
        if dummyNodeZero.next:
            newHead = dummyNodeZero.next;
        elif dummyNodeOne.next:
            newHead = dummyNodeOne.next;
        else:
            newHead = dummyNodeTwo.next;
        return newHead;
