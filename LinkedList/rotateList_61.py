class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        curr = head
        count = 0
        while curr and curr.next:
            count+=1
            curr = curr.next
        count+=1
        curr.next = head
        k = k%count
        new_k = count-k
        curr = head
        count1 = 1
        while count1<new_k:
            count1+=1
            curr = curr.next
        new_head = curr.next
        curr.next = None
        return new_head

    