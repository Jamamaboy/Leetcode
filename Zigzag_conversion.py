# import timeit

# numRows = 1000

# # Measure time for the first method
# time1 = timeit.timeit('[[0]*numRows]*numRows', globals=globals(), number=1000)

# # Measure time for the second method
# time2 = timeit.timeit('[[0] * numRows for _ in range(numRows)]', globals=globals(), number=1000)

# print(f"Time for first method: {time1}")
# print(f"Time for second method: {time2}")

class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows >= len(s) or numRows == 1:
			return s

		idx, d = 0, 1
		rows = [[] for _ in range(numRows)]

		for char in s:
			rows[idx].append(char)
			if idx == 0:
				d = 1
			elif idx == numRows - 1:
				d = -1
			idx += d

		for i in range(numRows):
			rows[i] = ''.join(rows[i])

		return ''.join(rows)

def convert(s,numRows):

	if numRows >= len(s) or numRows == 1:
		return s

	idx, d = 0, 1
	rows = [[] for _ in range(numRows)]

	for char in s:
		rows[idx].append(char)
		if idx == 0:
			d = 1
		elif idx == numRows - 1:
			d = -1
		idx += d

	for i in range(numRows):
		rows[i] = ''.join(rows[i])

	return ''.join(rows)

print(convert("1234567", 3))
