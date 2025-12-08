'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
      # code here
      newNode = Node(val);
      temp = head;
      
      if head == None:
          return newNode;
          
      if pos == 1:
          newNode.next = temp;
          return newNode;
    
      prevNode = None;
      nodeCounter = 1;
      while temp != None:
          if nodeCounter == pos:
              prevNode.next = newNode;
              newNode.next = temp;
              break;
          else:
              prevNode = temp;
              temp = temp.next;
              nodeCounter += 1;
              
      if temp == None:
          prevNode.next = newNode;
          newNode.next = temp;
      return head;
      
      
       
          
      
      