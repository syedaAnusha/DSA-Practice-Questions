# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(1)
    def reverseLL(self, node):
        newHead = None;
        while node != None:
            nextNode = node.next;
            node.next = newHead;
            newHead = node;
            node = nextNode;
        return newHead;

    
    def findKthNode(self, node, k):
        while node != None:
            if k == 1:
                return node;
            node = node.next;
            k -= 1;
        return node;
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        temp = head;

        while temp != None:
            kthNode = self.findKthNode(temp, k);
            if kthNode == None:
                # check if k = 0
                if prevNode:
                    prevNode.next = temp;
                break;
            nextNode = kthNode.next;
            kthNode.next = None;
            self.reverseLL(temp);
            if temp == head:
                head = kthNode;
            else:
                prevNode.next = kthNode;
            prevNode = temp;
            temp = nextNode;
                
        return head;        