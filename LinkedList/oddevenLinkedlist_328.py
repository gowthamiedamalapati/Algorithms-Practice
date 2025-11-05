class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return
        if not head.next:
            return head
        odd = head
        even = head.next
        head2= even
        while odd and even and  odd.next.next:
            odd.next = odd.next.next
            even.next = odd.next.next 
            odd = odd.next
            even = even.next 
        odd.next = head2
        return head
