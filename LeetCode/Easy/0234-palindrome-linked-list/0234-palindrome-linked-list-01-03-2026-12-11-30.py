# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)*O(k) + O(n)
    # Space Complexity: O(k)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head;
        palindromeStr = "";

        if temp.next == None:
            return True;
        
        if temp == None:
            return False;

        while temp != None:
            palindromeStr += str(temp.val);
            temp = temp.next;
        
        reverseStr = palindromeStr[::-1];

        if palindromeStr == reverseStr:
            return True;
        
        return False;
