class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
      temp1=head
      temp2=head.next

      while(temp2):
        temp=ListNode(math.gcd(temp1.val,temp2.val))
        temp.next=temp2
        temp1.next=temp

        temp1=temp2
        temp2=temp2.next

      return head
