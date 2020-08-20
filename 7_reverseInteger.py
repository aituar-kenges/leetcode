
class Solution():
	def reverse(self, x: int) -> int:
	    neg = 0
	    if (x<0):
	    	x *= -1
	    	neg = 1
	    res = 0
	    while(x>0):
	    	temp = x%10
	    	res = res*10+temp
	    	x = int(x/10)
	    if(neg):
	    	res*= -1
	    return res

t = Solution()
print (t.reverse(-123))