#User function Template for python3

def deleteHead(head):
    #code here
    temp = head;
    temp = temp.next;
    temp.prev = None;
    head.next = None;
    return temp;