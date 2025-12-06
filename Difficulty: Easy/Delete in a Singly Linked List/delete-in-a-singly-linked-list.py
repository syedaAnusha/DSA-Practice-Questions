'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if head == None:
            return head;
        if x == 1:
            head = head.next;
            return head;
        else:
            temp = head;
            countNode = 1;
            prevNode = None;
            while temp != None:
                if countNode == x:
                    prevNode.next = temp.next;
                    break;
                
                prevNode = temp;
                temp = temp.next;
                countNode += 1;
        return head;
        
