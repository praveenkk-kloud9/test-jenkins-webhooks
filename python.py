import unittest
import xmlrunner

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        print("Hello,")
        self.failUnless(IsOdd(1))

    def testTwo(self):
        print("World!")
        self.failIf(IsOdd(2))

def main():
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

if __name__ == '__main__':
    main()
