class Solution:
	def isPalindrome(self, s: str) -> bool:
		if s is None or len(s) == 0:
			return True

		s = s.lower() # to make it case insensitive

		l,r = 0, len(s)-1

		while l<r:
			#print("left - ",s[l],"|right - ",s[r])
			if any(lower <= ord(s[l]) <= upper for (lower, upper) in [(0,47),(58,96),(123,127)]):
				l = l+1
				continue
			elif any(lower <= ord(s[r]) <= upper for (lower, upper) in [(0,47),(58,96),(123,127)]):
				r = r-1
				continue
			elif s[l] != s[r]:
				return False
			else:
				l,r = l+1, r-1
		return True

		#efficient and easy to get solution from leetcode discussions
		# newStr = ""
		# for ch in s:
		# 	if ch.isalnum():
		# 		newStr+=ch.lower()
		# return newStr == newStr[::-1] # or newStr.reverse()


		#leetcode  - two-line solution
		# filteredChars = list(filter(lambda ch: ch.isalnum(), s.lower()))
		# return filteredChars == filteredChars[::-1]
s = Solution()

st = "A man, a plan, a canal: Panama"
print(s.isPalindrome(st))