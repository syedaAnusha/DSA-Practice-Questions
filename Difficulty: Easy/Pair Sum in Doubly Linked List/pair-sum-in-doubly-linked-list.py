from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    # Optimal Approach
    # Time Complexity: O(n/2) + O(n/2) = O(n)
    # Space Complexity: O(len of pairs of sum)
    def getLastNode(self, head):
        slow = head;
        fast = head;
        while fast.next != None and fast.next.next != None:
            slow = slow.next;
            fast = fast.next.next;
        if fast.next == None:
            return fast;
        else:
            return fast.next;
        
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        lastNode = self.getLastNode(head);
        frontNode = head;
        pairsArr = [];
        
        while frontNode.data < lastNode.data:
            Sum = frontNode.data + lastNode.data;
            if Sum > target:
                lastNode = lastNode.prev;
            elif Sum < target:
                frontNode = frontNode.next;
            else:
                pair = (frontNode.data, lastNode.data);
                pairsArr.append(pair);
                lastNode = lastNode.prev;
                frontNode = frontNode.next;
                
        return pairsArr;
