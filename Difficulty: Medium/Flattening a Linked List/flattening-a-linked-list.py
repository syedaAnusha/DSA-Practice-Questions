'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^n) + O(len(arr) log len(arr)) + O(len(arr))
    # Space Complexity: O(len of arr) + O(len of list)
    def traverseList(self, tempNode, arr):
        if not tempNode:
            return;
        self.traverseList(tempNode.next, arr);
        self.traverseList(tempNode.bottom, arr);
        arr.append(tempNode.data);
        return;
        
    def flatten(self, root):
        # code here
        if not root or not root.next or not root.bottom:
            return root;
            
        tempArr = [];
        self.traverseList(root, tempArr);
        tempArr.sort();
        newHead = Node(tempArr[0]);
        temp = newHead;
        
        for i in range(1, len(tempArr)):
            node = Node(tempArr[i]);
            temp.bottom = node;
            temp = temp.bottom;
        return newHead;