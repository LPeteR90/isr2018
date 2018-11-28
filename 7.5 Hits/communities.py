#!/usr/bin/env python
# encoding: utf-8
import json
import numpy
import networkx
import matplotlib.pylab as plt

# TODO Student: Read the Graph from 'valar-morghulis.gml.gz' using networkx
#               and convert it to an undirected graph.
# TODO Student: Use the method for community detection described in the
#               lecture until there are no more edges left in the graph.
#               Be sure to remove all matching edges in every iteration.
#               You are dealing with floating point numbers so deal with them properly!
# TODO Student: Do not use the implementation provided by networkx instead
#               role your own. You may use the proper centrality related
#               function though!
# TODO Student: Write the resulting tuple containing the number of iterations it took
#               and a list containing the number of components in every
#               iteration incl. iteration 0 (= initial number of components
#               in the graph) using the provided 'store_result' function.

def perform(graph):
  ''' Takes a given networkx.Graph and uses the method described in the lecture to
      perform community detection on the given graph. Returns a tuple
      containing the amount of iterations needed and a list containing the
      number of components/communities per iteration. '''

  undirected = graph.to_undirected()

  num_iterations = 0
  num_components_current = networkx.number_connected_components(undirected)
  num_components_per_iteration = [num_components_current]

  while num_components_current < len(undirected.nodes()):
    # print "num_current components: ", num_components_current, ", num nodes: ", len(undirected.nodes())

    for subgraph in networkx.connected_component_subgraphs(undirected):
      if len(subgraph.nodes()) == 1:
        continue

      edge_betweenness = networkx.edge_betweenness_centrality(subgraph)
      max_betweenness = max(edge_betweenness.itervalues())
      max_edges = [e for e in edge_betweenness if edge_betweenness[e] == max_betweenness]

      for e in max_edges:
        undirected.remove_edge(*e)
        # print "number of edges", undirected.number_of_edges()

    num_components_current = networkx.number_connected_components(undirected)
    num_components_per_iteration.append(num_components_current)

    # print "numcomponents: ", num_components_current, ", numcompiter: ", num_components_per_iteration
    num_iterations += 1

    # print num_iterations
  return (num_iterations, num_components_per_iteration)


def plot(number_of_iterations, number_of_components):
  ''' Plots the given results return from 'perform' and stores the resulting file in the submission folder. '''

  # TODO Student: Create a plot showing the number of components (y-axis) per iteration (x-axis) and label both axes accordingly.
  # TODO Student: Store the plot (as a PNG) in 'submission/communitites.png'.

  plt.figure(figsize=(10,6))
  plt.title("A2: Community Detection $Iterations = %d$" % number_of_iterations)
  plt.xlabel("Iteration number")
  plt.ylabel("Number of graph components")
  plt.plot(number_of_components, 'b-')
  plt.savefig("submission/communities.png")


if __name__ == '__main__':
  graph = networkx.read_gml('valar-morghulis.gml.gz', label='id')
  results = perform(graph.to_undirected())
  plot(*results)

  with open(u'submission/communities.json', 'w') as fh:
    json.dump(results, fh)
