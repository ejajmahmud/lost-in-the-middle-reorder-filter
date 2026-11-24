"""Tests for PrimacyRecencyReorderer."""
import unittest
from lost_in_the_middle_reorder_filter.core import PrimacyRecencyReorderer, ContextItem

class TestPrimacyRecencyReorderer(unittest.TestCase):
    def test_u_curve_reordering(self):
        items = [
            ContextItem("d1", "low", 1.0),
            ContextItem("d2", "med", 2.0),
            ContextItem("d3", "high2", 3.0),
            ContextItem("d4", "high1", 4.0),
        ]
        res = PrimacyRecencyReorderer.reorder(items)
        # Highest (d4) should be at head, second highest (d3) at tail
        self.assertEqual(res[0].item_id, "d4")
        self.assertEqual(res[-1].item_id, "d3")
