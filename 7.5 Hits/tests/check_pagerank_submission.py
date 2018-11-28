# encoding: utf-8
import os
import json
import unittest
import tests

class TestPageRankSubmission(unittest.TestCase):

  def test_if_pagerank_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'pagerank')))

  def test_if_pagerank_file_contains_results(self):
    tests.valid_json_file(u'pagerank')
    with open(tests.get_submission_location(u'pagerank'), 'r') as fh:
      l = json.load(fh)

    self.assertTrue(len(l) == 20)
    self.assertGreater(len(l[0]), 0)

  def test_if_pagerank_plot_exists(self):
    _plot = tests.get_plot_location(u'pagerank')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)
