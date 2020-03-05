import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.usd = Currency("dollars")
        self.eth = Currency("ethirium")

    def test_construct_relation(self):
        fakeTarget = self.usd
        fakeSource = self.eth
        relation = Relation(fakeSource, fakeTarget, 0.8)

        self.assertEqual("dollars", relation.source.name)
        self.assertEqual("ethirium", relation.target.name)


    def test_calculate_conversion(self):
        fakeTarget = self.usd
        fakeSource = self.eth
        relation = Relation(fakeSource, fakeTarget, 0.8)

        self.assertEqual(relation.convert(10), 8)


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
