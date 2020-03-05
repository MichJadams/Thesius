
class Currency(object):
    def __init__(self, name):
        self.name = name

class Relation(object):
    def __init__(self, source, target, ExchangeRate):
       self.source = source
       self.target = target
       self.ExchangeRate = ExchangeRate

    def invertExchangeRate(self):
        return 1 / self.ExchangeRate

    def convertSourceToTarget(self, quantity):
        return quantity * self.ExchangeRate

    def convertTargetToSource(self, quantity):
        return quantity / self.ExchangeRate

    def reverse(self):
        return Relation(self.target, self.source, self.invertExchangeRate())

class FullRelationalTree(object):
    def __init__(self, relationalArray):
        self.relationalArray = relationalArray 
        # makreu sure sorted alphabetically
        # code here to turn target array into an object with the {name : }

    def constructTree(self):
        header = ["|{0}|".format(sourceRelation.name) for _, sourceRelation in enumerate(self.sourceArray)]
        row = ""
        print(header)
        for _, targetRelation in enumerate(self.targetArray):
            row += "|{1}|".format(targetRelation.ExchangeRate)

if __name__ == "__main__":
    import unittest
    print("Thesius is testing.")
    class TestStringMethods(unittest.TestCase):
        
        def setUp(self):
            self.usd = Currency("usd")
            self.eth = Currency("eth")
            self.ltc = Currency("ltc")
            self.btc = Currency("btc")

        def createRelations(self):

            usd_to_usd = Relation(self.usd, usd, 1)
            usd_to_eth = Relation(self.usd, self.eth, 0.25)
            usd_to_ltc = Relation(self.usd, self.ltc, 1.5)
            usd_to_btc = Relation(self.usd, self.btc, 2)

            btc_to_usd = Relation(self.btc, self.btc, 1)
            btc_to_eth = Relation(self.btc, self.eth, 3.75)
            btc_to_usd = Relation(self.btc, self.ltc, 2.9)
            btc_to_usd = usd_to_btc.reverse()

            eth_to_eth = Relation(self.eth, self.etc, 1)
            eth_to_ltc = Relation(self.eth, self.ltc, 0.15)
            eth_to_usd = usd_to_eth.reverse()
            eth_to_btc = btc_to_eth.reverse()            

            ltc_to_ltc = Relation(self.ltc, self.ltc, 1)
            ltc_to_usd = usd_to_ltc.reverse()
            ltc_to_eth = eth_to_ltc.reverse()
            ltc_to_btc = btc_to_ltc.reverse()

        def test_construct_relation(self):
            fakeTarget = self.eth
            fakeSource = self.usd
            relation = Relation(fakeSource, fakeTarget, 0.8)

            self.assertEqual("usd", relation.source.name)
            self.assertEqual("eth", relation.target.name)

        def test_calculate_conversion(self):
            fakeTarget = self.usd
            fakeSource = self.eth
            relation = Relation(fakeSource, fakeTarget, 0.8)

            self.assertEqual(relation.convert(10), 8)

        def test_calculate_relation_tree(self):
            createRelations()
            relationMaker = FullRelationalTree()
            self.assertEqual(relation.convert(10), 8)

    unittest.main()

# some values we came up with
#	usd	    btc	   eth	    ltc
#usd	1.00			
#btc	2.00	1.00		
#eth	0.25	3.75	1.00	6.67
#ltc	1.50	2.90	0.15	1.00
