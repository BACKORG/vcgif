"""
This test is for config file
"""

import unittest, os

class PathTest(unittest.TestCase):
    def test_current_path(self):
        print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        
if __name__ == '__main__':
    unittest.main()