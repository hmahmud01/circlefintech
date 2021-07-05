import unittest
from main import findX

class Test(unittest.TestCase):

  def test_find_None(self):
    data = [['****']]
    result = findX(data)
    expect = None
    self.assertEqual(expect, result)
    print("Checked with 2d Array for None")

  def test_find_True(self):
    data = [['***'], ['*x']]
    result = findX(data)
    expect = True
    self.assertEqual(expect, result)
    print("Checked with 2d Array for X inside")


if __name__ == '__main__':
    unittest.main()