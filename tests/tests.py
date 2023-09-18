import unittest

from color_utils import lib

default_dark = """
    scheme: "Default Dark"
    author: "Chris Kempson (http://chriskempson.com)"
    base00: "181818"
    base01: "282828"
    base02: "383838"
    base03: "585858"
    base04: "b8b8b8"
    base05: "d8d8d8"
    base06: "e8e8e8"
    base07: "f8f8f8"
    base08: "ab4642"
    base09: "dc9656"
    base0A: "f7ca88"
    base0B: "a1b56c"
    base0C: "86c1b9"
    base0D: "7cafc2"
    base0E: "ba8baf"
    base0F: "a16946"
"""

def add_one(number: int) -> int:
    return number +1

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_one(9), 10, 'The sum is wrong.')


    def test_hex_to_eight_bit(self):
        result = lib.hex_to_u8("181818")
        self.assertEqual(result, 24, f"Expected 24, got {result}")
    
    def test_hex_to_rgb(self):
        result = lib.hex_to_rgb("a16946")
        self.assertEqual(result, (161, 105, 70), "Test Failed")

if __name__ == '__main__':
    unittest.main()