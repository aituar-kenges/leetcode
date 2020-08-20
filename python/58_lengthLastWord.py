class Solution():
	def lengthOfLastWord(self, s: str) -> int:
		res = 0
		if len(s) == 0:
			return res
		words = s.split()
		for word in words:
			try:
				res = len(word)
			except:
				return res
		return res

test = Solution()
print(test.lengthOfLastWord("Hello my name is sdaf;lkjaskd"))