'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    # Better Approach
    # Time Complexity: O(N*N*M)
    # Space Complexity: O(N) where for each horizontal nth node, flattenLists call only once
    def flattenLists(self, tempNode):
        if not tempNode or not tempNode.next:
            return tempNode;
        mergedHead = self.flattenLists(tempNode.next);
        return self.mergeLinkedLists(mergedHead, tempNode);
    
    def mergeLinkedLists(self, head1, head2):
        temp1 = head1;
        temp2 = head2;
        dummyNode = Node(-1);
        mover = dummyNode;
        while temp1 != None and temp2 != None:
            if temp1.data < temp2.data:
                mover.bottom = temp1;
                mover = mover.bottom;
                temp1 = temp1.bottom;
            else:
                mover.bottom = temp2;
                mover = mover.bottom;
                temp2 = temp2.bottom;
            mover.next = None;
        if temp1:
            mover.bottom = temp1;
        else:
            mover.bottom = temp2;
        return dummyNode.bottom;
                
        
    def flatten(self, root):
        # code here
        if not root or not root.next or not root.bottom:
            return root;
        return self.flattenLists(root);
