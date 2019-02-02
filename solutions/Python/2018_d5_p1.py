#This problem is very close to solving the word problem in a free group, this algorithm is based on the fact that
#Pushdown machines (those which accept/define context-free language) can solve the word problem for free groups.
#This (and a nice algebraic extension of this) is known as the muller-schupp theorem: https://en.wikipedia.org/wiki/Muller%E2%80%93Schupp_theorem
#Ask me if you want to know more.

#You might see that a stack suffices without doing all the group theory, it's just that the group theory
#is what made me think of this solution.

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