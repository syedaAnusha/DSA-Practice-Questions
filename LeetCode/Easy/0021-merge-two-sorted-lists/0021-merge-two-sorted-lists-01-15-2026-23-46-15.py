# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n1) + O(n2)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1);
        mover = dummyNode;
        temp1 = list1;
        temp2 = list2;

        if temp1 == None and temp2 == None:
            return None;
        
        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                mover.next = temp1;
                mover = temp1;
                temp1 = temp1.next;
            else:
                mover.next = temp2;
                mover = temp2;
                temp2 = temp2.next;

        if temp1 == None:
            mover.next = temp2;
        else:
            mover.next = temp1;
        
        return dummyNode.next;


        

        