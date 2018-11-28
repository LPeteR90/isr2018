# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import pagerank
import tests

class TestPageRankTask(unittest.TestCase):
  def setUp(self):
    pass

  def test_implementation_with_circle(self):
    graph = networkx.DiGraph([(1,2),(2,3),(3,4),(4,1)])
    ranks = pagerank.perform(graph)

    numpy.testing.assert_almost_equal(ranks.shape, (20, 4))
    [numpy.testing.assert_almost_equal(row, [.25, .25, .25, .25]) for row in ranks]

  def test_implementation_with_sink_and_source(self):
    graph = networkx.DiGraph([(0,1),(1,2),(2,3),(3,4),(4,1),(4,5)])
    ranks = pagerank.perform(graph)

    N = graph.number_of_nodes()
    initial_value = 1.0 / N

    numpy.testing.assert_almost_equal(ranks.shape, (20, N))

    numpy.testing.assert_almost_equal(ranks[0,:], N * [initial_value])

    # Nodes 0-4 will hand over most of their pagerank and...
    [self.assertLessEqual(sum(row[:-1]), (N - 1) * initial_value) for row in ranks]

    # .. the sink should absorb most of the pagerank.
    self.assertGreater(ranks[-1,-1], sum(ranks[-1,:-1]))

    # Source
    self.assertLess(ranks[-1,0], sum(ranks[-1,1:]))

    [numpy.testing.assert_almost_equal(sum(row), 1.) for row in ranks]

  def test_implementation_with_simple_example(self):
    graph = networkx.DiGraph(networkx.generators.scale_free_graph(25, seed=42))
    ranks = pagerank.perform(graph)

    numpy.testing.assert_almost_equal(ranks.shape, (20, 25))

    [numpy.testing.assert_almost_equal(sum(row), 1.) for row in ranks]

    expected_ranks = [  0,  1,  2, 19, 15, 12, 21, 18,  8, 22,
                        3,  4,  5,  6,  7,  9, 17, 10, 11, 23,
                       13, 14, 20, 16, 24 ]

    numpy.testing.assert_equal(expected_ranks, list(reversed(numpy.argsort(ranks[-2,:]))))
