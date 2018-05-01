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
class UndirectedNode(Node):
	def add_adjacency(self,adjacent_node):
		if adjacent_node not in self._adjacencies and self not in adjacent_node._adjacencies:
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

class DirectedNode(UndirectedNode):
	def add_adjacency(self,adjacent_node):
		if adjacent_node not in self._adjacencies:
			self._adjacencies.append(adjacent_node)
			return True
		else:
			return False
class UndirectedWeightedNode(Node):
	def add_adjacency(self,adjacent_node,weigth):
		if (adjacent_node,weigth) not in self._adjacencies and (self,weigth) not in adjacent_node._adjacencies:
			self._adjacencies.append((adjacent_node,weigth))
			return True
		else:
			return False
	def del_adjacency(self,adjacent_node,weigth):
		try:
			self._adjacencies.remove((adjacent_node,weigth))
			return True
		except:
			return False
class DirectedWeightedNode(UndirectedWeightedNode):
	def add_adjacency(self,adjacent_node,weigth):
		if (adjacent_node,weigth) not in self._adjacencies:
			self._adjacencies.append((adjacent_node,weigth))
			return True
		else:
			return False
	
