#!/usr/bin/env python
# encoding: utf-8
import json
import networkx
import numpy
from matplotlib.pylab import plt


# TODO Student: Implement PageRank as described in the lecture and implement the
#               "Scaled PageRank Update Rule" etc. Do not use any algorithm
#               implementation provided by networkx or numpy!
# TODO Student: Load the graph stored in 'valar-morghulis.gml.gz'.
# TODO Student: Run the graph through your PageRank implementation multiple
#               times and with 150 steps per run while varying 's' (see
#               slides) from 0.0 to 0.95 in steps of 0.05. Store the
#               resulting rank vector.
# TODO Student: Store the results from every run in a MxN Matrix, where M
#               represents the used 's' and N is the length of the rank vector.
# TODO Student: Create a plot showing the sensibility of the PageRank
#               algorithm with respect to 's'. Label the axes accordingly!
# TODO Student: Save this plot (as a PNG) in 'submissions/pagerank.png'
# TODO Student: Use '.tolist()' on the previously mentioned matrix and pass
#               the resulting list to the 'store_result' function.

def perform(graph):
  result = numpy.zeros((20, graph.number_of_nodes()))

  num_nodes = float(graph.number_of_nodes())

  for i, s in enumerate(numpy.arange(0.0, 1.0, 0.05)):
    networkx.set_node_attributes(graph, 'rank', 1.0 / num_nodes)
    networkx.set_node_attributes(graph, 'shares', 0.0)

    for k in range(0, 150):
      for n in graph.nodes():
        if(len(graph.successors(n)) > 0):
          share = graph.node[n]['rank'] / float(len(graph.successors(n)))
          for node in graph.successors(n):
            graph.node[node]['shares'] += share
        else:
          graph.node[n]['shares'] += graph.node[n]['rank']

      for n in graph.nodes():
        graph.node[n]['shares'] *= s
        graph.node[n]['shares'] += (1.0 - s) / num_nodes
        graph.node[n]['rank'] = graph.node[n]['shares']
        graph.node[n]['shares'] = 0.0

    for j, n in enumerate(graph.nodes()):
      result[i][j] = graph.node[n]['rank']

  return result


def plot(ranks):
  plt.figure(figsize=(20,10))
  plt.title("A2.3 PageRank (s-Sensibility)")
  plt.xlabel("Node ID")
  plt.ylabel("Pagerank")
  for row in ranks:
    plt.plot(row)


  plt.legend(['s = %.2f' %s for s in numpy.arange(0.0, 1.0, 0.05)], loc='upper right', prop={'size': 7})
  plt.savefig("submission/pagerank.png")


if __name__ == '__main__':
  graph = networkx.read_gml('valar-morghulis.gml.gz', label='id')
  results = perform(graph)
  plot(results)

  with open(u'submission/pagerank.json', 'w') as fh:
    json.dump(results.tolist(), fh)
