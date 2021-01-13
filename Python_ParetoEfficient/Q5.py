from Task3.Q5.Agent import Agent


def main():
	p1 = Agent()
	p2 = Agent()
	p3 = Agent()
	agents = [p1, p2, p3]
	# print(is_pareto_improvement(agents, 1, 2))
	all_opt = [1, 2, 3, 4, 5]
	is_pareto_optimal(agents, 6, all_opt)


def is_pareto_improvement(agents: list, option1: int, option2: int) -> bool:
	is_pareto_im = 0
	for i in range(len(agents)):
		opt1 = agents[i].eval(option1)
		opt2 = agents[i].eval(option2)
		if opt1 > opt2:  # if the first option is better,it is not pareto improvement
			is_pareto_im = 0
			break
		else:
			if opt1 < opt2:  # if it is better then the first option,it MIGHT be pareto improvement
				is_pareto_im = 1
	return bool(is_pareto_im)


def is_pareto_optimal(agents: list, option: int, all_options: list)->bool:
	for i in range(len(all_options)):
		if is_pareto_improvement(agents, option, all_options[i]):
			return bool(0)
	return bool(1)


if __name__ == "__main__":
	main()
