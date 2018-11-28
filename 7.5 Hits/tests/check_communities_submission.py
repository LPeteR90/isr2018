# encoding: utf-8
import os
import json
import unittest
import tests

class TestCommunitiesSubmission(unittest.TestCase):

  def test_if_communities_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'communities')))

  def test_if_communities_file_contains_results_tuple(self):
    self.assertTrue(tests.valid_json_file(u'communities'))
    with open(tests.get_submission_location(u'communities'), 'r') as fh:
      iterations, components = json.load(fh)

    self.assertTrue(type(iterations) == int)
    self.assertTrue(type(components) == list)

  def test_if_communities_plot_exists(self):
    _plot = tests.get_plot_location(u'communities')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)
