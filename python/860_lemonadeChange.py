class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:

        fives, tens, twenties = 0,0,0
        print(bills)
        for bill in bills:
        	if bill == 5:
        		fives+=1
        	elif bill == 10:
        		tens +=1
        		if fives>=1:
        			fives -=1
        		else:
        			return False
        	
        	elif bill == 20:
        		twenties+=1
        		if fives>=1 and tens>=1:
        			fives -=1
        			tens -=1
        		elif fives>=3 and tens ==0:
        			fives -=3
        		else:
        			return False   

        	print(fives, tens, twenties)     		
        
        return True
bills1 = [5,5,20,5,5,10,5,10,5,20]
sol = Solution()
print(sol.lemonadeChange(bills1))