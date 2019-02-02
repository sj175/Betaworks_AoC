from collections import defaultdict
import re

def parse_input():
	with open('2018_d5_input.txt', 'r') as f:
		return f.read().strip()


def reduce(problem_input):
	s = []
	for char in problem_input:
		if s and s[-1] == char.swapcase():
			s.pop()
		else:
			s.append(char)

	return len(s)

def get_alphabet():
	for i in range(26):
		yield chr(97 + i)


def main(problem_input):
	smallest_poly = 9999999999999
	char_to_remove = ''
	for char in get_alphabet():
		smallest_poly = min(reduce(problem_input.replace(char, '').replace(char.swapcase(), '')), smallest_poly)

	return smallest_poly


if __name__ == '__main__':
	print(main(parse_input()))