class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        if s is None or len(s)==0:
            return res
        
        #The idea is to go one character ch by one in string s, and
        #when inspecting some ch, start looping through its neighbours on both sides:
        #add 1 to a result res, whenever neigboring ch-s are the same, and b
        #break that inner loop, when condition is not satisfied
        
        # We need nested for loop #two-level#         
        i = 0
        fin = len(s)
        
        
        
        for ch in s:
            res +=1
            for i2 in range(1,i+1):
                print("in first check i2 - ", i2, "|ch = ", ch, "|res = ", res)
                if (i+i2)>=fin:
                    break
                elif s[i+i2] == s[i-i2]:
                    print(s[i], i2)
                    res += 1
                else:
                    break
            for i2 in range(i+1):
                print("in second check i2 - ", i2, "|ch = ", ch, "|res = ", res)
                if (i+i2+1)>=fin:
                    break                
                elif s[i-i2] == s[i+i2+1]:
                    res += 1 
                else:
                    break               
            i +=1
            
        return res
        
s = Solution()
st = "apaapa"
print (s.countSubstrings(st))