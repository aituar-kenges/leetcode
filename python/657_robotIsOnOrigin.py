class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontalDiscrepancy = 0
        verticalDiscrepancy = 0
        for move in moves:
            if move =="U":
                verticalDiscrepancy += 1
            elif move =="D":
                verticalDiscrepancy -= 1
            elif move =="L":
                horizontalDiscrepancy += 1
            elif move =="R":
                horizontalDiscrepancy -= 1 
            
        
        if horizontalDiscrepancy == 0 and verticalDiscrepancy == 0:
            return True
        else:
            return False