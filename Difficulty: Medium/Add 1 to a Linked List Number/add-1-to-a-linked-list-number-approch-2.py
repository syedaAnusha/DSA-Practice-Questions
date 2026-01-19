'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # Brute Force Approach - 2
    # Time Complexity: O(3n)
    # Space Complexity: O(1)
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
        carry = 1;
        
        while temp != None:
            temp.data = temp.data + carry;
            if temp.data < 10:
                carry = 0;
                break;
            else:
                temp.data = 0;
                carry = 1;
            temp = temp.next;
            
        if carry == 1:
            newNode = Node(carry);
            newHead =  self.reverseList(newHead);
            newNode.next = newHead;
            return newNode;
        
        return self.reverseList(newHead);
