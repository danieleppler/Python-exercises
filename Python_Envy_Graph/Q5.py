import networkx as nx
import matplotlib.pyplot as plt

from Task5.Agent import Agent


def main():
	a1 = Agent()
	a2 = Agent()
	a3 = Agent()

	agents = [a1, a2, a3]
	bundles1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

	g1 = nx.DiGraph()
	g1 = envy_graph(agents, bundles1)
	nx.draw(g1)
	plt.show()

	bundles2=[[1, 2], [3], [4, 5, 6]]

	g2 = nx.DiGraph()
	g2 = envy_graph(agents, bundles2)
	nx.draw(g2)
	plt.show()

	a4 = Agent()
	a5 = Agent()
	a6 = Agent()
	a7 = Agent()
	a8 = Agent()
	a9 = Agent()
	a10 = Agent()

	agents = agents + ([a4, a5, a6, a7, a8, a9, a10])
	bundles1 = bundles1 + ([[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],
	                 [37,38,39,40]])

	g3 = nx.DiGraph()
	g3 = envy_graph(agents, bundles1)
	nx.draw(g3)
	plt.show()

	bundles2 = bundles2 + ([[7],[8,9],[10,11],[12],[13,14,15],[16],[17,18,19]])

	g4 = nx.DiGraph()
	g4 = envy_graph(agents, bundles2)
	nx.draw(g4)
	plt.show()


def envy_graph(agents, bundles):
	g = nx.DiGraph()

	for q in range(len(agents)):
		g.add_node(q)

	for i in range(len(agents)):
		for j in range(len(agents)):
			if i != j:
				for k in range(len(bundles[j])):
					if agents[i].item_value(bundles[j][k]) > agents[j].item_value(bundles[j][k]):
						g.add_edge(i, j)    # i envy of j
						break
	return g


if __name__ == "__main__":
	main()