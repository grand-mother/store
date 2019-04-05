# -*- coding: utf-8 -*-
"""
Unit tests for the grand_store.protocol module
"""

import unittest

from grand_store.protocol import InvalidBLOB, get


class ProtocolTest(unittest.TestCase):
    """Unit tests for the protocol module"""

    def test_get(self):
        # Test the end-to-end chain
        blob = get("check.txt")
        self.assertEqual(blob, b"This is just a check\n")

        # Test the wrong url case
        with self.assertRaises(InvalidBLOB) as context:
            blob = get("toto")


if __name__ == "__main__":
    unittest.main()
