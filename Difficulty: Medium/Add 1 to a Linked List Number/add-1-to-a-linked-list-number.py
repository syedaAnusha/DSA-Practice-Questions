'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # Optimal Approach
    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    # Aux Space for stack recursion: O(n)
    def addOneToList(self, head):
        if head == None:
            return 1;
        
        carry = self.addOneToList(head.next);
        Sum = head.data + carry;
        head.data = Sum % 10; 
        carry = Sum // 10;
        return carry;
        
    def addOne(self,head):
        if head == None:
            return None;
       
        carry = self.addOneToList(head);
        if carry == 1:
            newHead = Node(carry);
            newHead.next = head;
            return newHead;
        return head;
        