class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        # the idead is to 
        
        if len(nums)==0:
            return 0
        
        res, res2, size = 1, 1, len(nums)
        m = 0
        for i in range(size):
            for i2 in range(m, size):
                m = i2
                if nums[i2+1]>size:
                    break
                if nums[i2]<nums[i2+1]:
                    res2 += 1
                else:
                    break
            if res2>res:
                res = res2
            res2 = 1            
            
        
        return res