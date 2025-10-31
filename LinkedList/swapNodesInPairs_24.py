class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head  or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        prev_conn = dummy
        curr = head
        while curr and curr.next:
            nxt = curr.next.next
            curr.next.next = curr
            prev_conn.next =  curr.next
            curr.next = nxt
            prev_conn = curr
            curr = nxt
        return dummy.next