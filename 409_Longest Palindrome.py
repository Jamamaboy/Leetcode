# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

from collections import Counter
class Solution:
	def longestPalindrome(self, s: str) -> int:
		c = Counter(s)
		flag = False
		ans = 0
		for i in c.keys():
			if c[i]%2==0:
				ans+=c[i]
			else:
				if not flag:
					flag = True
					if c[i]>2:
						ans+=(c[i]-1)
				else:
					if c[i]>2:
						ans+=(c[i]-1)

		return ans+flag


if __name__ == "__main__":
	solution = Solution()
	test_string = "abccccdd"
	print(solution.longestPalindrome(test_string))
