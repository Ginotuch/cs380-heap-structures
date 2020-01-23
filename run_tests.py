"""
Runs all unittests in the ./tests directory
code source: https://stackoverflow.com/a/40437679/4432618
Author: slaughter98 (stackoverflow username)
"""
import unittest
loader = unittest.TestLoader()
start_dir = 'tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
