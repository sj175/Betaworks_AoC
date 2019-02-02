def parse_input():
	with open('2018_d1_p1_input.txt', 'r') as f:
		return f.read().split("\n")

def main(txt_input):
	current = 0
	for line in txt_input:
		if line[0] == '-':
			current -= int(line[1:])
		else:
			current += int(line[1:])

	return current

if __name__ == '__main__':
	print(main(parse_input()))