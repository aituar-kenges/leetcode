
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        if l1 == None and l2 == None:
        	return res
        elif l1 == None:
        	l1.val = 0
        elif l2 == None:
        	l2.val = 0
        res.val = l1.val+l2.val
        solu = Solution()
        res.next = solu.addTwoNumbers(l1.next, l2.next)
        return res
li1_1 = ListNode(3)
li1_2 = ListNode(4)
li1_3 = ListNode(1)
li1_1.next = li1_2
li1_2.next = li1_3
li2_1 = ListNode(1)
li2_2 = ListNode(5)
#li2_3 = ListNode(2)
li2_1.next = li2_2
#li2_2.next = li2_3
sol = Solution()
solution = sol.addTwoNumbers(li1_1, li2_1)
while not solution == None:
	print (solution.val)
	solution = solution.next