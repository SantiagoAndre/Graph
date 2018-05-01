from node import *
class Graph:
	def __init__(self):
		self._nodes = []
	def nodes(self):
		return self._nodes
	def add_node(self, element):
		new_node = self.create_node(element)
		if new_node in self.nodes():
			raise Exception("Node %s already in graph" %  element)
		else:
			self.nodes().append (new_node)
	def del_node(self, element):
		try:
			self.nodes().remove(self.create_node(element))
		except:
			raise Exception("Node %s not in graph" % element)
	def _get_node(self, element):
		for node in	self._nodes:
			if node.element() == element:
				return node
	def __str__(self):
		pass
			

class UndirectedGraph(Graph):
	def create_node(self,element):
		return UndirectedNode(element)
	def edges(self):
		edges = []
		for node in self.nodes():
			for adjacency in node.adjacencies():
				edges.append((node,adjacency))
		return edges
	def add_edge(self, edge):
		init_element,fnl_element = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.add_adjacency(fnl_node)
		if not success:
			raise Exception("Edge {0} already in graph".format(edge))
	def del_edge(self, edge):
		init_element,fnl_element = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.del_adjacency(fnl_node)
		if not success:
			success = fnl_node.del_adjacency(init_node)
			if not success:
				raise Exception("Edge {0} not in graph".format(edge))
	
class DirectedGraph(UndirectedGraph):
	def create_node(self,element):
		return DirectedNode(element)

		return edges
	def del_edge(self, edge):
		init_element,fnl_element = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.del_adjacency(fnl_node)
		if not success:
			raise Exception("Edge {0} not in graph".format(edge))
class UndirectedWeightedGraph(Graph):
	def create_node(self,element):
		return UndirectedWeightedNode(element)
	def edges(self):
		edges = []
		for node in self.nodes():
			for adjacency,weigth in node.adjacencies():
				edges.append((node,adjacency,weigth))
		return edges
	def add_edge(self, edge):
		init_element,fnl_element,weigth = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.add_adjacency(fnl_node,weigth)
		if not success:
			raise Exception("Edge {0} already in graph".format(edge))
	def del_edge(self, edge):
		init_element,fnl_element,weigth = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.del_adjacency(fnl_node,weigth)
		if not success:
			success = fnl_node.del_adjacency(init_node,weigth)
			if not success:
				raise Exception("Edge {0} not in graph".format(edge))
class DirectedWeightedGraph(UndirectedWeightedGraph):
	def create_node(self,element):
		return DirectedWeightedNode(element)
	def del_edge(self, edge):
		init_element,fnl_element,weigth = edge
		init_node = self._get_node(init_element)
		fnl_node = self._get_node(fnl_element)
		if init_node is  None:
			raise Exception("Node %s not in graph" % init_element)
		if fnl_node is  None:
			raise Exception("Node %s not in graph" % fnl_element)
		success = init_node.del_adjacency(fnl_node,weigth)
		if not success:
			raise Exception("Edge {0} already in graph".format(edge))
