from Task12.Agent import Agent
import networkx as nx


def main():
	a=Agent
	b=Agent
	c=Agent
	d=Agent
	a.preferences=[1,4,3,2]
	a.current_shift=3
	a.name="Yoel"
	b.preferences=[3,2,1,4]
	b.current_shift=2
	b.name="Avi"
	c.preferences=[2,4,1,3]
	c.current_shift=1
	c.name="Gili"
	d.preferences=[3,4,2,1]
	d.current_shift=4
	d.name="Yosi"
	workers = [a, b, c, d]
	exchange_shifts(workers)


def exchange_shifts(workers):
	g=nx.DiGraph()
	for i in range(len(workers)):
		g.add_node(i)
	for i in range(len(workers)):
		for j in range(len(workers[i].preferences)):
			g.add_edge(i, workers[i].preferences[j])
	while len(g) != 0:
		cycles = nx.simple_cycles(g)
		c = [cycle for cycle in cycles]
		for i in range(len(c)):
			if len(c[i]) != 0 and len(c[i]) != 1:
				temp = c[i][0]
				for j in range(len(c[i])-1):
					print(workers[c[i][j]].name + " move from shift "+workers[c[[i][j]]].current_shift
					      + "    to  " + workers[c[i][j+1]].current_shift)
					g.remove_node(c[i][j])
				print(workers[c[i][len(c)-1]].name + " move from shift " + workers[c[i][len(c)-1]].current_shift + "    to  " + temp)
				g.remove_node(c[i][len(c[i])-1])


if __name__ == '__main__':
	main()
	import doctest
	doctest.testmod()