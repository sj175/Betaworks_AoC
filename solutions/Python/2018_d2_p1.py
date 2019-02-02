from collections import defaultdict

def parse_input():
	with open('2018_d2_p1_input.txt', 'r') as f:
		return f.read().split("\n")

def process_line(line):
	two = False
	three = False
	occurences = defaultdict(int)
	for char in line:
		occurences[char] += 1

	for _, v in occurences.items():
		if v == 2:
			two = True
		if v == 3:
			three = True

	return two, three

def main(my_input):
	two_sum = 0
	three_sum = 0
	for line in my_input:
		two, three = process_line(line)
		two_sum += two
		three_sum += three

	return two_sum * three_sum

if __name__ == '__main__':
	print(main(parse_input()))