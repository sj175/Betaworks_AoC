import datetime
from collections import defaultdict

def parse_input():
	with open('2018_d3_input.txt', 'r') as f:
		return f.read().split("\n")


def process_claim(claim, grid):
	claim = claim.split(" ")
	ords = tuple(map(int, claim[2].replace(":", "").split(",")))
	size = tuple(map(int, claim[3].split("x")))

	for i in range(size[0]):
		for j in range(size[1]):
			grid[ords[0] + i][ords[1] + j] += 1


def main(problem_input):
	grid = [ [0]*1000 for _ in range(1000) ]
	for line in problem_input:
		process_claim(line, grid)

	total = 0
	for i in range(1000):
		for j in range(1000):
			if grid[i][j] > 1:
				total += 1

	return total


if __name__ == '__main__':
	start = datetime.datetime.now()
	print(main(parse_input()))
	end = datetime.datetime.now()
	print(end - start)