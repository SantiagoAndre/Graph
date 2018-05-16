class Node:
	def __init__(self, element):
		self._element = element
		self._adjacencies = []
	def element(self):
		return self._element
	def adjacencies(self):
		return self._adjacencies
	def set_element(self, new_element):
		self._element= new_element
	def __str__(self):
		return str(self.element())
	def __repr__(self):
	    return str(self)
	def __eq__(self, other):
		return self.element() == other.element()

class DirectedNode(Node):
	def add_adjacency(self,adjacent_node):
		if not self.exist_adjacency(adjacent_node):
			self._adjacencies.append(adjacent_node)
			return True
		else:
			return False
	def del_adjacency(self,adjacent_node):
		try:
			self._adjacencies.remove(adjacent_node)
			return True
		except:
			return False
	def exist_adjacency(self,other_node):
		return other_node  in self.adjacencies()
class UndirectedNode(DirectedNode):
	def del_adjacency(self,adjacent_node):
		success = super().del_adjacency(adjacent_node)
		if success:
			return True
		try:
			adjacent_node._adjacencies.remove(self)
			return True
		except:
			return False
	def exist_adjacency(self,other_node):
		return other_node  in self.adjacencies() or self  in other_node.adjacencies()
class DirectedWeightedNode(Node):
	def add_adjacency(self,adjacent_node,weigth):
		if not self.exist_adjacency(adjacent_node,weigth):
			self._adjacencies.append((adjacent_node,weigth))
			return True
		else:
			return False
	def del_adjacency(self,adjacent_node,weigth):
		try:
			self.adjacencies().remove((adjacent_node,weigth))
			return True
		except:
			return False
	def exist_adjacency(self, other_node,weigth):
		return (other_node,weigth)  in self.adjacencies()
class UndirectedWeightedNode(DirectedWeightedNode):
	def del_adjacency(self,adjacent_node,weigth):
		success = super().del_adjacency(adjacent_node,weigth)
		if success:
			return True
		try:
			adjacent_node.adjacencies().remove((self,weigth))
			return True
		except:
			return False
	def exist_adjacency(self, other_node,weigth):
		return (other_node,weigth)  in self.adjacencies() or (self,weigth)  in other_node.adjacencies()
