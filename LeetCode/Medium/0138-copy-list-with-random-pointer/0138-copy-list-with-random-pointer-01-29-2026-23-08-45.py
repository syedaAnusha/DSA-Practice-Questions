"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Optimal Approach - My code
    # Time Complexity: O(n) + O(n) + O(n) = O(3n)
    # Space Complexity: O(n)   
    def insertCopyNodesBetweenOriginalList(self, head):
        temp = head;
        while temp != None:
            copyNode = Node(temp.val);
            copyNode.next = temp.next;
            temp.next = copyNode;
            temp = temp.next.next;
        return head;
    
    def connectRandomPointerWithCopyNode(self, head):
        temp = head;
        while temp != None:
            copyNode = temp.next;
            if not temp.random:
                copyNode.random = None;
            else:
                copyNode.random = temp.random.next;
            temp = temp.next.next;
        return head;
    
    def extractDeepCopy(self, head):
        dummyNode = Node(-1);
        temp = head;
        mover = dummyNode;
        while temp != None:
            copyNode = temp.next;
            mover.next = copyNode;
            temp.next = copyNode.next;
            mover = mover.next;
            temp = temp.next;
        return dummyNode.next;
    

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None;
        self.insertCopyNodesBetweenOriginalList(head);
        self.connectRandomPointerWithCopyNode(head);
        return self.extractDeepCopy(head);