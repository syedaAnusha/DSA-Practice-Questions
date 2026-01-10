# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        if head == None or (n == 1 and head.next == None):
            return None;   

        fastPtr = head;
        slowPtr = head;

        for i in range(n):
            fastPtr = fastPtr.next;
        
        if fastPtr == None:
            newHead = head.next;
            return newHead;
        
        while fastPtr.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next;
           
        slowPtr.next = slowPtr.next.next;
        return head;
         