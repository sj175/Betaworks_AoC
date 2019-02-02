def parse_input():
	with open('2018_d5_input.txt', 'r') as f:
		return f.read().strip()


def main(problem_input):
	s = []
	for char in problem_input:
		if s and s[-1] == char.swapcase():
			s.pop()
		else:
			s.append(char)

	return len(s)


if __name__ == '__main__':
	print(main(parse_input()))