# encoding: utf-8
import os
import json
import unittest
import tests

class TestHitsSubmission(unittest.TestCase):

  def test_if_hits_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'hits')))

  def test_if_hits_file_contains_results_tuple(self):
    tests.valid_json_file(u'hits')
    with open(tests.get_submission_location(u'hits'), 'r') as fh:
      hubs, authorities = json.load(fh)

    self.assertTrue(type(hubs) == dict)
    self.assertTrue(type(authorities) == dict)

  def test_if_hits_plot_exists(self):
    _plot = tests.get_plot_location(u'hits')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)
