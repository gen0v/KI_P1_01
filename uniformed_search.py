# Task 1.1: Route planning in Romania
# You are to solve a route planning problem in Romania. To do so, please use the file graph.py and utils.py.
# Implement
# BFS
# DFS
# UCS
# For your solution, please provide the path and the costs for travelling from Bucharest to Timisoara.

from queue import Queue, LifoQueue, PriorityQueue
from graph import Node, Edge, Graph
from utils import getNode

romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
] )

class Search:
   def __init__(self, graph: Graph):
      self.graph = graph

   def bfs(self, spt, ept) -> tuple:
      node = spt
      if node == ept:
         return (node,0)
      frontier = Queue()
      frontier.put(node)
      explored = []
      while 1:
         #print("---")
         if frontier.empty():
            return(node.name,0)
         node = frontier.get()
         explored.append(node)
         for edge in node.edges:
            child = edge.end
            #print(child.path)
            if child not in explored:
               #save the edge
               child.path = child.path + node.path
               child.path.append(edge)
               child.value = node.value + edge.value
               if child == ept:
                  print (child.path)
                  return (child.name, child.value)
               frontier.put(child)
               
      


search = Search(romania)
print(search.bfs(romania.getNode("Bu"), romania.getNode("Ti")))