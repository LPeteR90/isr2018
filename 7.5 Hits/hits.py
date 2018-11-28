#!/usr/bin/env python
# encoding: utf-8
import json
import math
import networkx
import matplotlib.pylab as plt

def perform(graph, iterations=100):
  ''' Runs the HITS algorithm (as described in the lectures) on a given
      networkx.Graph and returns the hubs and authority scores for all
      nodes.'''

  # TODO Student: Implement and run the HITS algorithm (as described in the lectures)
  #               on a given networkx.Graph. Do not use the networkx functionality.
  # TODO Student: Do not forget to normalize your scores (see slides)!

  networkx.set_node_attributes(graph, 'hub', 1.0)
  networkx.set_node_attributes(graph, 'auth', 1.0)

  # for node in graph.nodes():
  #   node['hub'] = 1
  #   node['auth'] = 1

  # update iterations times
  for i in range(0, iterations):
    # authority update
    for n in graph.nodes():
      sum = 0
      for node in graph.predecessors(n):
        sum += graph.node[node]['hub']
      graph.node[n]['auth'] = sum

    # hub update
    for n in graph.nodes():
      sum = 0
      for node in graph.successors(n):
        sum += graph.node[node]['auth']
      graph.node[n]['hub'] = sum

  # normalize
  total_auth = 0
  total_hub = 0
  for node in graph.nodes():
    total_auth += graph.node[node]['auth']
    total_hub += graph.node[node]['hub']

  hubs, authorities = {}, {}
  for node in graph.nodes():
    graph.node[node]['auth'] /= total_auth
    authorities[node] = graph.node[node]['auth']
    graph.node[node]['hub'] /= total_hub
    hubs[node] = graph.node[node]['hub']

  return (hubs, authorities) # (hubs, authorities)

def plot(hubs, authorities):
  ''' Plots the given results returned from 'perform' and stores the resulting file in the submission folder. '''

  # TODO Student: Create a plot showing the hub and authority scores (y-axis) for every node and label both axes accordingly.
  # TODO Student: Store the plot (as a PNG) in 'submission/hits.png'.

  plt.figure(figsize=(10,6))
  plt.title("A2: Hubs & Authorities")
  plt.xlabel('Node ID')
  plt.ylabel('Score')
  plt.plot(hubs.values(), label='hubs')
  plt.plot(authorities.values(), label='authorities')
  plt.legend(['hubs', 'authorities'], loc='upper left', prop={'size': 10})

  plt.savefig("submission/hits.png")


if __name__ == '__main__':
  graph = networkx.read_gml('valar-morghulis.gml.gz', label='id')
  results = perform(graph)
  plot(*results)

  with open(u'submission/hits.json', 'w') as fh:
    json.dump(results, fh)
