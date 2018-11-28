# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import hits
import tests

class TestHitsTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.DiGraph()
    self._graph.add_edges_from([(1,3),(1,5),(2,1),(3,5),(5,4),(5,3),(6,5)])
    self._authorities = dict(zip(self._graph,[0.000000, 0.000000, 0.366025, 0.133975, 0.500000, 0.000000]))
    self._hubs = dict(zip(self._graph,[0.366025, 0.000000, 0.211325, 0.000000, 0.211325, 0.211325]))

    self._results = hits.perform(self._graph)
    self.assertEqual(len(self._results), 2)
    self.hubs, self.authorities = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self.hubs), type({}))
    self.assertEqual(type(self.authorities), type({}))

  def test_if_hub_values_match_expectations(self):
    self.assertGreater(len(self.hubs), 0)
    self.assertEqual(len(self.hubs), len(self._hubs))
    for n in self._graph:
      numpy.testing.assert_almost_equal(self.hubs[n], self._hubs[n], decimal=4)

  def test_if_authority_values_match_expectations(self):
    self.assertGreater(len(self.authorities), 0)
    self.assertEqual(len(self.authorities), len(self._authorities))
    for n in self._graph:
      numpy.testing.assert_almost_equal(self.authorities[n], self._authorities[n], decimal=4)
