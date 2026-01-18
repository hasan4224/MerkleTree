# test_merkletree.py
"""
Tests for MerkleTree module.
"""

import unittest
from merkletree import MerkleTree

class TestMerkleTree(unittest.TestCase):
    """Test cases for MerkleTree class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MerkleTree()
        self.assertIsInstance(instance, MerkleTree)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MerkleTree()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
