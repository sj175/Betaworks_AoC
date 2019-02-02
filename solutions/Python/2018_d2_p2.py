from collections import defaultdict

def parse_input():
	with open('2018_d2_p1_input.txt', 'r') as f:
		return f.read().split("\n")

def process_strings(str1, str2):
	if len(str1) != len(str2):
		return False

	seen_a_difference = False
	for i, c in enumerate(str1):
		if c != str2[i]:
			if seen_a_difference:
				return False
			else:
				seen_a_difference = True
	return True

def difference(str1, str2):
	"""We know theres only one difference so find it"""
	for i, c in enumerate(str1):
		if str2[i] != c:
			if i < len(str1) - 1:
				return str1[:i] + str1[i+1:]
			return str1[:-1]

def main(my_input):
	for i, line in enumerate(my_input):
		for line2 in my_input[i + 1:]:
			if process_strings(line, line2):
				return difference(line, line2)

	return None

if __name__ == '__main__':
	print(main(parse_input()))