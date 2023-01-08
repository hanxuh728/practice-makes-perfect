class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # i = 0
        # arr = [head]
        # while arr[i].next != None:
        #     arr.append(arr[i].next)
        #     i += 1

        # if n == i+1:
        #     return head.next
        # elif n == 1:
        #     arr[i-1].next = None
        # else:
        #     arr[i-n].next = arr[i-n+2]
            
        # return head
        first = head
        second = head
        for i in range(n):
            first = first.next

        if first == None:
            return head.next
        else:
            while first.next != None:
                first = first.next
                second = second.next
            second.next = second.next.next
            return head