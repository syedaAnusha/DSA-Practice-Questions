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
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(len of pairs of sum)
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        ithNode = head;
        pairsArr = [];
        
        while ithNode != None:
            jthNode = ithNode.next;
            while jthNode != None:
                Sum = ithNode.data + jthNode.data;
                if Sum == target:
                    pair = (ithNode.data, jthNode.data);
                    pairsArr.append(pair);
                jthNode = jthNode.next;
            ithNode = ithNode.next;
        return pairsArr;
