from __future__ import print_function, unicode_literals
from unittest import TestCase
import logging
from datetime import datetime
from gridmap import Job, process_jobs

import microbe_toolbox

class TestJoke(TestCase):
    def test_is_string(self):
        s = microbe_toolbox.joke()
        self.assertTrue(isinstance(s, basestring))

class TestGrid(TestCase):
    def test_mr(self):
        """Function to test if standard grid scheduling is working"""
        print("OGE Map-Reduce Test...")
        logging.captureWarnings(True)
