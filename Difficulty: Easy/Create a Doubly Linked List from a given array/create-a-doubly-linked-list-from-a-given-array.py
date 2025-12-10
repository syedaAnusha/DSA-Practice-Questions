'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
   def createDLL(self, arr):
     # code here
     head = Node(arr[0]);
     temp = head;
     
     for i in range(1, len(arr)):
         node = Node(arr[i]);
         temp.next = node;
         node.prev = temp;
         temp = node;
     return head;
     