import unittest
from couch import Couch
from rabbit import Rabbit

class TestSuite(unittest.TestCase):

    def test(self):
        couch = Couch()
        couch.populate()
        things = couch.count()
        self.failIf(things != 5)
        
    def test(self):
        rabbit = Rabbit()
        rabbit.sendMessage()
        things = rabbit.relayMessage()
        self.failIf(things != "Hello World!")


def main():
    unittest.main()

if __name__ == "__main__":
    main()
