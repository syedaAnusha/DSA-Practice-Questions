# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(1)
    def findLenOfLL(self, node):
        cnt = 0;
        temp = node;
        while temp != None:
            cnt += 1;
            temp = temp.next;
        return cnt;

    def getSecondLastNode(self, node, k):
        secondLastNode = node;
        lastNode = node;
        k -= 1;
        while k >= 0:
            lastNode = lastNode.next;
            k -= 1;
        while lastNode.next != None:
            secondLastNode = secondLastNode.next;
            lastNode = lastNode.next;
        return (secondLastNode, lastNode);
             
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head;
        temp = head;
        k = k % self.findLenOfLL(temp);
        nodes = self.getSecondLastNode(temp, k);
        lastNode = nodes[0]
        newHead = nodes[1];
        newHead.next = head;
        head = lastNode.next;
        lastNode.next = None;
        return head;        