import os

class MindMapComposite:
	SHAPES = {
		"circle": "(({}))",
		"oval": "({})",
		"square": "[{}]",
		"cloud": "){}(",
		"hexagon": "{{{{{}}}}}",
		"bang": ")){}(("
	}

	def __init__(self, name, shape):
		self.name = name
		self.shape = shape
		self.children = []

	def __str__(self):
		return self.get_shape_representation().format(self.name)

	def add(self, child):
		self.children.append(child)

	def remove(self, child):
		self.children.remove(child)

	def get_shape_representation(self):
		return self.SHAPES.get(self.shape, "{}")

	def display(self, indent=0):
		print("    " * indent + str(self))
		for child in self.children:
			child.display(indent+1)