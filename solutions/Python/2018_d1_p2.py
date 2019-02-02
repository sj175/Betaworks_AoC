def parse_input():
	with open('2018_d1_p1_input.txt', 'r') as f:
		return f.read().split("\n")

def main(txt_input):
	seen = set()
	current = 0
	seen.add(0)
	while(True):
		for line in txt_input:
			current += int(line)
			if current in seen:
					return current
			seen.add(current)

if __name__ == '__main__':
	print(main(parse_input()))