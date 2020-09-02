"""---------------------------------------

Unit Testing
------------

* Test small pieces of the component in isolation (units)
* Lots of built-in assertions to use in the tests
* Inherit from unittest.TestCase

Format, using assertEqual:
--------------------------

self.assertEqual(
    <function>(<param>, <param>),
    <result>
)

----------------------------------------"""

import unittest
from testing_unittests_funcs import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    
    def test_eat_healthy(self):
        """
        Eat should have a positive message for healthy eating.
        """
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because it's a healthy thing."
        )

    def test_eat_unhealthy(self):
        """Eat should have a negavite message cause you're a fatass."""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )

    def test_short_nap(self):
        """Short naps are better."""
        self.assertEqual(
            nap(1),
            "Feeling refreshed."
        )

    def test_long_nap(self):
        """Long naps usually backfire."""
        self.assertEqual(
            nap(3),
            "Damn. Overslept."
        )

    def test_is_funny_tim(self):
        """Tim's just not funny."""
        self.assertFalse(is_funny("tim"), "tim should not be funny")
    
    def test_is_funny_others(self):
        """Anyone else but tim should be funny."""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        self.assertIn(
            laugh(),
            ('lol', 'haha', 'tehehe')
        )

    def test_eat_healhty_bool(self):
        """is_healthy must be a Boolean."""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares")

if __name__ == "__main__":
    unittest.main()