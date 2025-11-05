class Solution(object):
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            nxt1 = curr1.next
            curr1.next = curr2
            nxt2 = curr2.next
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
        return head
