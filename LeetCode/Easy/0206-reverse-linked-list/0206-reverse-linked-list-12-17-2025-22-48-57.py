# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Compexity: O(n)
    # Space Compexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        
        temp = head;
        prevNode = None;
        while temp != None:
            nextNode = temp.next;
            temp.next = prevNode;
            prevNode = temp;
            temp = nextNode;
        
        return prevNode;
        