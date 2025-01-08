class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1 or numRows >= len(s):
			return s

		# Initialize rows
		rows = [''] * numRows
		curRow, goingDown = 0, False

		# Iterate over characters in s
		for c in s:
			rows[curRow] += c
			# Change direction at the first or last row
			if curRow == 0 or curRow == numRows - 1:
				goingDown = not goingDown
			curRow += 1 if goingDown else -1

		# Join rows to form the final string
		return ''.join(rows)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))              # Output: "A"
