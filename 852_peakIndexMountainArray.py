class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        peak = 0
        
        for i in range(len(A)):
            if A[i]>A[i+1]:
                break
            if A[i]<A[i+1]:
                peak = i+1
            
        return peak 
            