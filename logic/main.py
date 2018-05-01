from graphs import *
def testGraph(graph):
	graph.add_node(1)
	graph.add_node(2)
	graph.add_node(3)
	graph.add_node(4)
	graph.add_node(5)
	graph.del_node(1)
	graph.add_edge((2,2))
	graph.add_edge((2,3))
	graph.add_edge((2,2))
	graph.add_edge((3,4))
	graph.add_edge((3,4))
	print (graph.edges())
	graph.del_edge((3,2))
	graph.del_edge((3,3))
def testWeightedGraph(graph):
	graph.add_node(1)
	graph.add_node(2)
	graph.add_node(3)
	graph.add_node(4)
	graph.add_node(5)
	graph.del_node(1)
	graph.add_edge((2,2,1))
	graph.add_edge((2,3,9))
	graph.add_edge((2,2,2))
	graph.add_edge((3,4,1))
	graph.add_edge((3,4,34))
	print (graph.edges())
	graph.del_edge((3,2,1))
	graph.del_edge((3,3,1))
def load_file():
	from file_graph import *
	if 'T' not in locals():
		T = 1

	if T == 1:
		print("Undirected Graph")
		graph = UndirectedGraph()
	elif T == 2:
		print("Directed Graph")
		graph = DirectedGraph()
	elif T == 3:
		print("Undirected Weighted Graph")
		graph = UndirectedWeightedGraph()
	elif T == 4:
		print("Directed Weighted Graph")
		graph = DirectedWeightedGraph()
	else:
		raise Exception("invalid graph type")
		
	if 'N'  in locals():
		for node in N:
			graph.add_node(node)
	if 'E' in locals():
		for edge in E:
			graph.add_edge(edge)
	return graph
if __name__== "__main__":
	try:
		graph = load_file()
		print(graph.nodes())
		print(graph.edges())
	except Exception as ex:
		print(ex)
