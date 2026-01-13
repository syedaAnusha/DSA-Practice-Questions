# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(2n) + O(nlogn)
    # Space Complexity: O(n)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        tempArr = [];
        temp = head;
        while temp != None:
            tempArr.append(temp.val);
            temp = temp.next;
        
        tempArr.sort();
        temp = head;
        for i in range(len(tempArr)):
            temp.val = tempArr[i];
            temp = temp.next;
        return head;