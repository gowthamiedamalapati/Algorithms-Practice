class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        end = ListNode(0,head)
        curr = head
        head1 = end
        while curr and curr.next:
            if curr.val != curr.next.val:
                end = end.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                end.next = curr.next
            curr = curr.next
        return head1.next
