import unittest

from aubrey_fortune_area.cli import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting(self) -> None:
        self.assertEqual(greeting("Aubrey"), "Hello, Aubrey! Welcome to AubreyFortuneArea.")


if __name__ == "__main__":
    unittest.main()
