class Solution(object):
    def reverseBetween(self, head, left, right):
        count = [1]
        curr = head
        start_prev = None
        while count[0] < left and curr:
            start_prev = curr
            curr = curr.next
            count[0]+=1

        def reverse(curr,start_prev):
            prev = None
            reverse_start = curr   
            while curr and count[0] <= right: 
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count[0]+=1
            if start_prev:
               start_prev.next = prev
            reverse_start.next = curr  
            return prev
        new_head = reverse(curr,start_prev)
        return head if left > 1 else new_head #i.e when left = 1 we start reversing from fisrt node and returning head will
        