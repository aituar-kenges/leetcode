
def subtractProductAndSum(self, n: int) -> int:
        
#         if n == 0:
#             return 0
        
#         n = abs(n)
        
    sumD, prodD = 0, 1 
        
        
        # while n > 0:
        #     lastDigit = n%10 
        #     sumD += lastDigit
        #     prodD *= lastDigit
        #     n //= 10

    for digit in [int(d) for d in str(n)]:
        sumD += digit
        prodD *= digit
      
           
    return prodD - sumD


