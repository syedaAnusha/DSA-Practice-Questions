# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach - 2
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(1)
    def findLenAndTailOfLL(self, node):
        totalNodes = 1;
        tail = node;
        while tail.next != None:
            totalNodes += 1;
            tail = tail.next;
        return [totalNodes, tail];
    
    def findNthNode(self, head, k):
        temp = head;
        cnt = 1;
        while temp != None:
            if cnt == k:
                return temp;
            temp = temp.next;
            cnt += 1;
        return temp;
          
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head;

        result = self.findLenAndTailOfLL(head);
        totalNodes = result[0];
        tailNode = result[1];
        k = k % totalNodes;
        if k == 0:
            return head;
        
        tailNode.next = head;
        newLastNode = self.findNthNode(head, totalNodes - k);
        head = newLastNode.next;
        newLastNode.next = None;
        return head;        