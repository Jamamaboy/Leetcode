def two_sum(nums, target):
	for i in range(0, len(nums)):
		for j in range(0, len(nums)):
			if nums[i] + nums[j] == target:
				return i, j
	return 0


def two_sum2(nums, target):
	map = {}

	for i, num in enumerate(nums):
		map[num] = i

	for i, num in enumerate(nums):
		t = target - num
		if t in map and i != map[t]:
			return [i, map[t]]

	return [-1, -1]

def main():
	input_nums = []
	int1 = 1
	while (int1):
		int1 = (input("nums : "))
		if(int1):
			input_nums.append(int(int1))
	input_target = int(input("target : "))

	print(two_sum2(input_nums, input_target))

main()
