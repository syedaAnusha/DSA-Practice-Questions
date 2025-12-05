'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        temp = head;
        while temp != None:
            if temp.data == key:
                return True;
            temp = temp.next;
        return False;
        