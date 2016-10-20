import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# if __name__ == '__main__':
#     unittest.main()

# Testsuit is collection of testcase and testsuit
test_suit = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner().run(test_suit)
