import multibind as mb
import matplotlib.pyplot as plt
import networkx as nx

c = mb.Multibind()
c.read_graph("examples/input/4-state-diamond/graph.csv",comment="#")
c.read_states("examples/input/4-state-diamond/states.csv")
c.build_cycle()
res = c.MLE()
