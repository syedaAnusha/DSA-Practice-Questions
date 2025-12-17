# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach - Recursive
    # Time Compexity: O(n)
    # Space Compexity: O(n) for aux space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        
        else:
            newHead = self.reverseList(head.next);
            frontNode = head.next;
            frontNode.next = head;
            head.next = None;
            return newHead;