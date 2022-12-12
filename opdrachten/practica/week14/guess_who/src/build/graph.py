from py2neo import Graph, Node, Relationship

graph = Graph()
alex = Node("Person", name="Alex")
graph.create(alex)