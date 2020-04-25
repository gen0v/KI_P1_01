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

import heapq
     


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
      self.backup_graph = graph
      #self.graph.Print()

   def reset(self):
      for n in self.graph.nodes:
         n.reset()

   def dfs(self, spt, ept) -> tuple:
      self.reset()
      node = spt
      if node == ept:
         return (0,[])
      frontier = LifoQueue()
      frontier.put(node)
      explored = []
      while 1:
         if frontier.empty():
            return(node.value,node.path)
         node = frontier.get()
         explored.append(node)
         for edge in node.edges:
            child = edge.end
            child.path = []
            if child not in explored:
               #save the edge
               child.path = child.path + node.path
               child.path.append(edge)
               child.value = node.value + edge.value
               if child == ept:
                  return (child.value, child.path)
               frontier.put(child)

   def bfs(self, spt, ept) -> tuple:
      self.reset()
      node = spt
      if node == ept:
         return (0,[])
      frontier = Queue()
      frontier.put(node)
      explored = []
      while 1:
         if frontier.empty():
            return(node.value,node.path)
         node = frontier.get()
         explored.append(node)
         for edge in node.edges:
            child = edge.end
            child.path = []
            if child not in explored:
               #save the edge
               child.path = child.path + node.path
               child.path.append(edge)
               child.value = node.value + edge.value
               if child == ept:
                  return (child.value, child.path)
               frontier.put(child)
   
   def ucs(self, spt, ept) -> tuple:
      self.reset()
      node = spt
      if node == ept:
         return (0,[])
      heap = []
      path = []
      heapq.heappush(heap, node)
      explored = []
      while 1:
         #print("---")
         if len(heap) == 0:
            return(node.value,path)
         node = heapq.heappop(heap)
         # print("Going to " + node.name)
         explored.append(node)
         if node == ept:
            node.value = 0
            for ed in node.path:
               node.value+=ed.value
            return (node.value, node.path)
         for edge in node.edges:
            child = edge.end
            # print("Child = " + child.name)
            # ("Childvalue = " + str(child.value))
            if child not in explored and child not in heap:
               child.path = child.path + node.path
               child.path.append(edge)
               #save the edge
               #needs to stay else heap not working
               child.value = node.value + edge.value
               # print("Pushing " + child.name)
               heapq.heappush(heap,child)
            elif child in heap:
               newvalue = node.value + edge.value
               # find and replace if value smaller and heapify
               count = 0
               for x in heap:
                  if x.name == child.name:
                     if x.value > newvalue:
                        # print("Replacing : " + str(x.value) + " with " + str(newvalue))
                        #replace
                        # print("Replacing " + x.name + " with " + child.name)
                        # Overwrite childpath
                        child.path = node.path
                        # save the edge
                        # needs to stay else heap not working
                        child.path.append(edge)
                        # Overwrite child.value
                        child.value = node.value + edge.value
                        # replace with cheaper way
                        heap[count] = child
                        # heapify the heap as it is broken because of replacing
                        heapq.heapify(heap)
                        
                     else:
                        break
                  count += 1
            # for x in heap:
            #    print(x.name + " " + str(x.value))
            # print("---")


               
      

   
def __repr__(self):
   return (self.start.name + " --> " + self.end.name)

def __lt__N(self, other: Node):
   return self.value < other.value

def __lt__E(self, other: Edge):
   return self.value < other.value

def reset(self: Node):
   self.value = 0
   self.path = []

setattr(Node,"__lt__",__lt__N)
setattr(Node,"reset",reset)
setattr(Edge,"__lt__",__lt__E)
setattr(Edge,"__repr__",__repr__)
setattr(Node,"path",[])

search = Search(romania)

print("BFS from BU to TI")
print(search.bfs(getNode("Bu",romania.nodes), getNode("Ti",romania.nodes)))

print("DFS from BU to TI")
print(search.dfs(getNode("Bu",romania.nodes), getNode("Ti",romania.nodes)))

print("UCS from BU to TI")
print(search.ucs(getNode("Bu",romania.nodes), getNode("Ti",romania.nodes)))
