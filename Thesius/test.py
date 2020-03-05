
class demo(object):
    def __init__(self):
        self.rates = {}
    
    def setRatio(self, source, target, exchangeRate):
        if source not in self.rates:
            self.rates[source] = {}
        self.rates[source][target] = exchangeRate
    
    def constructTree(self, root, value, depth=0):
        if depth >= 3:
            return
        spacer = "  "*depth
        print(spacer+"table for", root, "valued", value)
        for currency in self.rates[root]:
            tradeValue = self.rates[root][currency]*value
            print(spacer+"  Can Trade", currency, "for", tradeValue)
            self.constructTree(currency, tradeValue, depth+1)

d = demo()
d.setRatio("usd", "btc", 0.5)
d.setRatio("usd", "eth", 4)

d.setRatio("btc", "usd", 2)
d.setRatio("btc", "eth", 0.27)

d.setRatio("eth", "usd", 0.25)
d.setRatio("eth", "btc", 3.75)

d.constructTree("usd", 10)