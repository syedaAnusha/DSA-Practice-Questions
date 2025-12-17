# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Compexity: O(n) + O(n) = O(2n)
    # Space Compexity: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;

        tempArr = [];
        temp = head;
        while temp != None:
            tempArr.append(temp.val);
            temp = temp.next;
        
        temp = head;
        while temp != None:
            temp.val = tempArr.pop();
            temp = temp.next;
        
        return head;
        