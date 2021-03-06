from collections import defaultdict
import re

def parse_input():
	with open('2018_d4_input.txt', 'r') as f:
		return sorted(f.read().replace('[', '').replace(']', '').split("\n"))

def separate_days(lines):
	output = []
	current = []
	for i in range(0, len(lines)):
		if "Guard" in lines[i]:
			output.append(current)
			current = []

		current.append(lines[i])

	return output[1:]


def main(problem_input):
	sleep = defaultdict(lambda: [0] * 60)
	night_shifts = separate_days(problem_input)
	for night_shift in night_shifts:
		guard_id = night_shift[0].split(" ")[3].replace('#', '')
		for i in range(len(night_shift)):
			info_line = night_shift[i].split(" ")
			if info_line[2] == "falls":
				sleep_start = int(info_line[1].split(":")[1])
				sleep_stop = int(night_shift[i + 1].split(" ")[1].split(":")[1])
				for j in range(sleep_start, sleep_stop):
					sleep[guard_id][j] += 1

	sleepy_max = 0
	sleepy_guard = -1
	for guard_id, sleep_list in sleep.items():
		total = sum(sleep_list)
		if sleepy_max < total:
			sleepy_guard = guard_id
			sleepy_max = total

	sleepiest_minute = sleep[sleepy_guard].index(max(sleep[sleepy_guard]))

	return sleepy_guard, sleepiest_minute



if __name__ == '__main__':
	print(main(parse_input()))