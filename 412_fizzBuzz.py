class Solution:
    def fizzBuzz(self, n: int):
        res = list()
        if n<1:
        	return res
        for i in range(n+1):
        	if i ==0:
        		continue
        	if i%15==0:
        		res.append("FizzBuzz")
        	elif i%3==0:
        		res.append("Fizz")
        	elif i%5==0:
        		res.append("Buzz")
        	else:
        		res.append(str(i))
        return res

a = Solution()
print(a.fizzBuzz(15))

            
