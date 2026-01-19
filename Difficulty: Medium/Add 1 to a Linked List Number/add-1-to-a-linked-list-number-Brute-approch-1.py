'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(n)
    def reverseList(self, head):
        prevNode = None;
        temp = head;
        while temp != None:
            frontNode = temp.next;
            temp.next = prevNode;
            prevNode = temp;
            temp = frontNode;
        return prevNode;
        
    def addOne(self,head):
        if head == None:
            return head;
        #Returns new head of linked List.
        newHead = self.reverseList(head);
        temp = newHead;
        dummyNode = None;
        nodeOne = Node(1);
        carry = 0;
        mover = dummyNode;
        
        while temp != None or nodeOne != None:
            Sum = carry;
            if temp != None:
                Sum += temp.data;
            if nodeOne != None:
                Sum += nodeOne.data;
            newNode = Node(Sum % 10);
            newNode.next = mover;
            mover = newNode;
            carry = Sum // 10;
            
            if temp:
                temp = temp.next;
            if nodeOne:
                nodeOne = nodeOne.next;
        if carry:
            newNode = Node(carry);
            newNode.next = mover;
            mover = newNode;
            
        return mover;
