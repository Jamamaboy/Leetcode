import timeit
# from memory_profiler import memory_usage
#pip install memory-profiler psutil

class Solution:
	def rob1(self, nums: list[int]) -> int:
		n = len(nums)

		if n <= 2:
			return max(nums)

		dp = [0] * n
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])

		for i in range(2, n):
			dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

		return dp[-1]

	def rob2(self, nums: list[int]) -> int:
		tmp_l = []
		for i, n in enumerate(nums):
			if i < 2:
				tmp_l.append(n)
			else:
				max_val = max(tmp_l[:-1])
				tmp_l.append(max_val + n)
		return max(tmp_l)

	def rob3(self, nums: list[int]) -> int:
		dp = [0] * (len(nums) + 1)
		if len(nums) == 1:
			return nums[0]

		dp[1] = nums[0]

		for i in range(2, len(dp)):
			dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

		return dp[-1]



# Generate a test case
import random
nums = [random.randint(1, 100) for _ in range(1000)]

# Create a solution object
solution = Solution()

# Measure the time taken and memory used by rob1
def run_rob1():
	solution.rob1(nums)

time_rob1 = timeit.timeit(run_rob1, number=10)
# memory_rob1 = max(memory_usage((run_rob1,)))

# Measure the time taken and memory used by rob2
def run_rob2():
	solution.rob2(nums)

time_rob2 = timeit.timeit(run_rob2, number=10)
# memory_rob2 = max(memory_usage((run_rob2,)))

# Measure the time taken and memory used by rob3
def run_rob3():
	solution.rob3(nums)

time_rob3 = timeit.timeit(run_rob3, number=10)
# memory_rob3 = max(memory_usage((run_rob3,)))

print(f"rob1 - Time: {time_rob1:.5f} sec")
print(f"rob2 - Time: {time_rob2:.5f} sec")
print(f"rob3 - Time: {time_rob3:.5f} sec")

Ranking = [time_rob1, time_rob2, time_rob3]
R = sorted(Ranking)

# สร้าง dictionary เพื่อเก็บอันดับของแต่ละค่า
ranking_dict = {value: index + 1 for index, value in enumerate(R)}

# ใช้ dictionary เพื่อหาอันดับของแต่ละค่าใน Ranking
Name_Ranking = [ranking_dict[value] for value in Ranking]

print(Name_Ranking)
