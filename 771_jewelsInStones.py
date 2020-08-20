class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for i1 in J:
        	for i2 in S:
        		if i1==i2:
        			res +=1
        return res
