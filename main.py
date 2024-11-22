from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
	if __name__ == "__main__":
		# Root of the mindmap
		root = MindMapComposite( "Burgerland", "circle" )

		events = MindMapComposite( "Important Events", "oval" )
		
		tea = MindMapComposite( "Independence from Tea-land", "oval" )
		tea.add(MindMapLeaf("Discovery that tea tastes bad", "rectangle"))
		events.add( tea )
		
		war = MindMapComposite("The Bullet Wars", "oval")
		war.add(MindMapLeaf("Whoever shot the most bullets first won", "rectangle"))
		war.add(MindMapLeaf("So successful that they decided to make the Bullet Wars an Annual Event", "rectangle"))
		war.add(MindMapLeaf("15 casualties to date.", "rectangle"))
		events.add( war )
		
		burger = MindMapComposite( "Invention of the Burger", "oval" )
		burger.add(MindMapLeaf("11,900,867 casualties", "rectangle"))
		events.add( burger )
		
		root.add( events )
		
		root.display()


if __name__ == "__main__":
	main()
