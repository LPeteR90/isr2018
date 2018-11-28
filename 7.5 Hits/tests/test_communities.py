# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import communities
import tests

class TestCommunitiesTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.Graph()
    self._graph.add_edges_from([(1,2),(1,3),(2,3),(3,7),
                                (4,5),(4,6),(6,5),(6,7),
                                (9,10),(10,11),(11,9),(9,8),
                                (12,13),(13,14),(14,12),(12,8),
                                (7,8)])
    self._results = communities.perform(self._graph)
    self._number_of_iterations = 3
    self._number_of_components = numpy.array([1, 2, 6, 14])

    self.assertEqual(len(self._results), 2)
    self.number_of_iterations, self.number_of_components = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self._number_of_iterations),
                     type(self.number_of_iterations))
    self.assertEqual(type(self.number_of_components), type([]))

  def test_if_number_of_iterations_matches_expectation(self):
    self.assertGreater(self.number_of_iterations, 0)
    numpy.testing.assert_almost_equal(self.number_of_iterations,
                                      self._number_of_iterations)

  def test_if_number_of_components_match_expectations(self):
    self.assertGreater(len(self.number_of_components), 0)
    self.assertEqual(len(self.number_of_components), self._number_of_components.size)
    numpy.testing.assert_almost_equal(self.number_of_components,
                                      self._number_of_components)
