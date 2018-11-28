# encoding: utf-8
import os
import sys
import json
import numpy
import unittest
import networkx
sys.path.append(os.path.abspath('..'))

def skip_plot(*args, **kwargs):
  ''' The Lannister's send their regards. '''
  pass

def get_submission_location( task):
  ''' Returns the full path to a task's submission file. '''
  return os.path.join(os.getcwd(), u'submission', u'%s.json' % task)

def get_plot_location(task):
  ''' Returns the full path to a task's plot. '''
  return os.path.join(os.getcwd(), u'submission', u'%s.png' % task)

def valid_json_file(task):
  ''' Raises a ValueError iff the given task file doesn't contain valid json. '''
  with open(get_submission_location(task), 'r') as fh:
    if json.load(fh):
      return True

  return False
