# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head;
        strArr = [];

        if temp.next == None:
            return True;
        
        if temp == None:
            return False;

        while temp != None:
            strArr.append(temp.val);
            temp = temp.next;
        
        temp = head;
        while temp != None:
            if temp.val == strArr.pop():
                temp = temp.next;
                continue;
            else:
                return False

        return True;
