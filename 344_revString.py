class Solution:
    def reverseString(self, s:[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s2 = list(s)
        # fi = 0
        # li = len(s)
        # li -=1
        # while fi<li:
        # 	print(s2[fi], s2[li])
        # 	temp = s2[fi]
        # 	s2[fi] = s2[li]
        # 	s2[li] = temp 
        # 	fi+=1
        # 	li-=1
        # print(s2)
        # s = s2
        # print (s)
        s = s[::-1]
        print(s)
temp = Solution()
a = "Aiuar"
a = temp.reverseString(a)
print(a)