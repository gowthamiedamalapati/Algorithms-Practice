class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def partition(self, head, x):
        start = ListNode(0,None)
        head1 = start
        temp = ListNode(0,None)
        head2 = temp
        curr = head
        while curr:
            if curr.val < x:
                start.next = curr
                start = curr
            else:
                temp.next = curr
                temp = curr
            curr = curr.next
        temp.next = None
        start.next = head2.next
        return head1.next
