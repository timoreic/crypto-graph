# Student Name: Timo Reichelt
# Student ID:   19663858
# testHarness.py - Test Harness for classes.py

# Import Modules
import json
from classes import *

############################################################
# INITIALISING TRADING PAIRS | EDGE INFO | SORTED LINKED LISTS
############################################################

# Initialise Trading Pairs
ETHBTC = TradingPair("ETHBTC", "ETH", "BTC")
BNBBTC = TradingPair("BNBBTC", "BNB", "BTC")
BNBETH = TradingPair("BNBETH", "BNB", "ETH")
BTCUSDT = TradingPair("BTCUSDT", "BTC", "USDT")
ETHUSDT = TradingPair("ETHUSDT", "ETH", "USDT")

allPairs = LinkedList()
for tp in allPairs:
    allPairs.insertLast(TradingPair(
        tp.data.symbol, tp.data.baseAsset, tp.data.quoteAsset))

allPairs.insertLast(ETHBTC)
allPairs.insertLast(BNBBTC)
allPairs.insertLast(BNBETH)
allPairs.insertLast(BTCUSDT)
allPairs.insertLast(ETHUSDT)
try:
    with open("testTradeData.json", 'r') as f:
        datastore2 = json.load(f)
except:
    print("\nTrade data could not be loaded...")

for i in range(len(datastore2)):
    for pair in allPairs:
        if pair.data.symbol == datastore2[i]["symbol"]:
            pair.data.setBidPrice(datastore2[i]["bidPrice"])
            pair.data.setBidQty(datastore2[i]["bidQty"])
            pair.data.setAskPrice(datastore2[i]["askPrice"])
            pair.data.setAskQty(datastore2[i]["askQty"])
            pair.data.setHighPrice(datastore2[i]["highPrice"])
            pair.data.setLowPrice(datastore2[i]["lowPrice"])
            pair.data.setVolume(datastore2[i]["volume"])
            pair.data.setOpenPrice(datastore2[i]["openPrice"])
            pair.data.setLastPrice(datastore2[i]["lastPrice"])
            pair.data.setPriceChange(
                datastore2[i]["priceChange"])
            pair.data.setPriceChangePercent(
                datastore2[i]["priceChangePercent"])
            pair.data.setSpread(
                datastore2[i]["askPrice"], datastore2[i]["bidPrice"])


############################################################
# MAIN
############################################################
print("\n######## TEST HARNESS ########")

# Initialise Graph
testGraph = Graph()
print("\ntestGraph initialised")

# Copy allPairs to testGraph.tradingPairs
testGraph.tradingPairs = allPairs

# Add vertices
for pair in testGraph.tradingPairs:
    testGraph.addVertex(pair.data.quoteAsset)
    testGraph.addVertex(pair.data.baseAsset)
    print("vertex added")

# Test display
print("\n#### Test display: Expected output = list of all asset names")
testGraph.display()

# Test hasVertex
print("\n#### Test hasVertex: Expected output = True")
print(testGraph.hasVertex("BTC"))

# Test getVertex
print("\n#### Test getVertex: Expected output = BTC")
print(testGraph.getVertex("BTC"))

# Test delVertex
print("\n#### Test delVertex: Expected output = False")
testGraph.delVertex("BTC")
print(testGraph.hasVertex("BTC"))

# Test addEdges
print("\n#### Test addEdges: Expected output = List of all assets + edges (incl. exchange price and volume)")
for pair in testGraph.tradingPairs:
    testGraph.addVertex(pair.data.quoteAsset)
    testGraph.addVertex(pair.data.baseAsset)
print("\nall vertices added again...")

for i in range(testGraph.tradingPairs.size()):
    testGraph.addEdge(testGraph.tradingPairs.findIndex(i).data.symbol, testGraph.tradingPairs.findIndex(i).data.baseAsset, testGraph.tradingPairs.findIndex(
        i).data.quoteAsset, testGraph.tradingPairs.findIndex(i).data.bidPrice, testGraph.tradingPairs.findIndex(i).data.askPrice, testGraph.tradingPairs.findIndex(i).data.volume)
print("and edges added to graph!\n")

# Test display with edges
print(testGraph.display())

# Test findPath fast
print("\n#### Test findPath: Expected output = List of all possible paths")
path = LinkedList()
fast = True
print(testGraph.findPath("BTC", "USDT", path, fast))

# Test findPath not fast
print("\n#### Test findPath: Expected output = List of all possible paths + prices")
path = LinkedList()
fast = False
print(testGraph.findPath("BTC", "USDT", path, fast))
print("********************************************************************************\n\nCheapest Path: " +
      testGraph.bestPath + "\n\n********************************************************************************")
