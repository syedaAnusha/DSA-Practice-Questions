# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Lets assume N = n1 + n2;
    # Time Complexity: O(n1) + O(n2) + O(N log N) + O(N)
    # Space Complexity: O(N) + O(N)
    def convertArrToLL(self, arr):
        head = ListNode(arr[0]);
        temp = head;
        for i in range(1, len(arr)):
            node = ListNode(arr[i]);
            temp.next = node;
            temp = temp.next;
        return head;

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempArr = [];
        temp1 = list1;
        temp2 = list2;
        if temp1 == None and temp2 == None:
            return None;

        while temp1 != None:
            tempArr.append(temp1.val);
            temp1 = temp1.next;
        
        while temp2 != None:
            tempArr.append(temp2.val);
            temp2 = temp2.next;
        
        tempArr.sort();
        newHead = self.convertArrToLL(tempArr);
        return newHead;


        