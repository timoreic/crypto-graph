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

# Initialise Linked List
testList = LinkedList()
print("\ntestList initialised")

# Insert Last
print("\n\n#### Insert Last")
testList.insertLast(1)
print("inserted 1")
testList.insertLast(2)
print("inserted 2")
testList.insertLast(3)
print("inserted 3")
testList.insertLast(4)
print("inserted 4")
testList.insertLast(5)
print("inserted 5")
testList.insertLast(6)
print("inserted 6")

# Test __str__
print("\n#### Test __str__: Expected output = 1, 2, 3, 4, 5, 6,")
print(testList)

# Test testList.print()
print("\n#### Test testList.print(): Expected output = -> 1 -> 2 -> 3 -> 4 -> 5 -> 6")
print(testList.print())

# Test testList.size()
print("\n#### Test testList.size(): Expected output = 6")
print(testList.size())

# Test testList.peekFirst()
print("\n#### Test testList.peekFirst(): Expected output = 1")
print(testList.peekFirst())

# Test testList.peekLast()
print("\n#### Test testList.peekLast(): Expected output = 6")
print(testList.peekLast())

# Test testList.removeLast()
print("\n#### Test testList.removeLast(): Expected output for testList.peekLast() = 5")
testList.removeLast()
print(testList.peekLast())

# Test testList.isEmpty()
print("\n#### Test testList.isEmpty: Expected output = False")
print(testList.isEmpty())

# Test testList.getNode(4)
print("\n#### Test testList.getNode(4): Expected output = 4")
print(testList.getNode(4))

# Test testList.remove(2)
print("\n#### Test testList.remove(2): Expected output for testList.print() = 1, 3, 4, 5,")
testList.remove(2)
print(testList)

# Test testList.findIndex(2)
print("\n#### Test testList.findIndex(2): Expected output = 4")
print(testList.findIndex(2))

# Test __iter__
print("\n#### Test __iter__: Expected output = 1 3 4 5")
for node in testList:
    print(node)

# Initialise EdgeInfo(vertex, rate, symbol, volume)
print("\n#### Initialise EdgeInfo for sorted insertion")
edge1 = EdgeInfo(1, 1, "e1", 10)
print("edgeInfo1 initialised")
edge2 = EdgeInfo(3, 3, "e3", 30)
print("edgeInfo2 initialised")
edge3 = EdgeInfo(2, 2, "e2", 20)
print("edgeInfo3 initialised")
edge4 = EdgeInfo(4, 4, "e4", 40)
print("edgeInfo4 initialised")
testList = LinkedList()

# Test insertSorted()
print("\n#### Test insertSorted: Expected output for print(testList) = 1, 2, 3, 4,")
testList = LinkedList()
testList.insertSorted(edge1)
print("edge1 inserted")
testList.insertSorted(edge2)
print("edge2 inserted")
testList.insertSorted(edge3)
print("edge3 inserted")
testList.insertSorted(edge4)
print("edge4 inserted")
print(testList)

# Sorted Linked Lists
topVolume = LinkedList()
topPrice = LinkedList()
topPriceChange = LinkedList()
lowestSpread = LinkedList()
highestSpread = LinkedList()

for pair in allPairs:
    topVolume.insertSortedTopVolume(pair.data)
    topPrice.insertSortedTopPrice(pair.data)
    topPriceChange.insertSortedTopPriceChange(pair.data)
    lowestSpread.insertSortedLowSpread(pair.data)
    highestSpread.insertSortedHighSpread(pair.data)

# Test insertSortedTopVolume()
print("\n#### Test insertSortedTopVolume: ")
i = 0
while i < 5:
    print(str(i+1) + ": " +
          str(topVolume.findIndex(i).data.symbol) + ": " + str(topVolume.findIndex(i).data.volume))
    i += 1

# Test insertSortedTopPrice()
print("\n#### Test insertSortedTopPrice:")
i = 0
while i < 5:
    print(str(i+1) + ": " +
          str(topPrice.findIndex(i).data.symbol) + ": " + str(topPrice.findIndex(i).data.lastPrice))
    i += 1

# Test insertSortedTopPriceChange()
print("\n#### Test insertSortedTopPriceChange:")
i = 0
while i < 5:
    print(str(i+1) + ": " +
          str(topPriceChange.findIndex(i).data.symbol) + ": " + str(topPriceChange.findIndex(i).data.priceChangePercent))
    i += 1

# Test insertSortedLowSpread()
print("\n#### Test insertSortedLowSpread:")
i = 0
while i < 5:
    print(str(i+1) + ": " +
          str(lowestSpread.findIndex(i).data.symbol) + ": " + str(lowestSpread.findIndex(i).data.spread))
    i += 1

# Test insertSortedHighSpread()
print("\n#### Test insertSortedHighSpread:")
i = 0
while i < 5:
    print(str(i+1) + ": " +
          str(highestSpread.findIndex(i).data.symbol) + ": " + str(highestSpread.findIndex(i).data.spread))
    i += 1

# Test removeHighSpread()
print("\n#### Test removeHighSpread:")
highestSpread = LinkedList()

for pair in allPairs:
    highestSpread.removeHighSpread(pair)

for i in range(round(highestSpread.size()/2)):
    highestSpread.findIndex(i).data = "X"
    print("Trade Pair removed!")

# Test insertSortedHighSpread()
print("\n#### Test insertSortedHighSpread after removing high spread trade pairs:")

allPairs = highestSpread
highestSpread = LinkedList()

for pair in allPairs:
    if pair.data != "X":
        highestSpread.insertSortedHighSpread(pair.data.data)
        print(pair.data.data.symbol + ": " + pair.data.data.spread)

print("\nBNBETH and BNBBTC removed")
