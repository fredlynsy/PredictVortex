# test_predictvortex.py
"""
Tests for PredictVortex module.
"""

import unittest
from predictvortex import PredictVortex

class TestPredictVortex(unittest.TestCase):
    """Test cases for PredictVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PredictVortex()
        self.assertIsInstance(instance, PredictVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PredictVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
