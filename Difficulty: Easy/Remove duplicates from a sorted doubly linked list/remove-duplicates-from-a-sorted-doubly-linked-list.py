'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if head == None or head.next == None:
            return head;
            
        temp = head;
        while temp.next != None:
            if temp.data == temp.next.data:
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