# Student Name: Timo Reichelt
# Student ID:   19663858
# cryptoGraph.py - Classes for cryptoGraph.py

#### Index ####

# 1: List Node
# 2: Linked List
# 3: Edge Info
# 4: Trading Pair
# 5: Graph Vertex
# 6: Graph


#### Classes ####

############################################################
# 1: List Node
############################################################
class ListNode():

    # INIT
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    # STRING
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __str__(self):
        return str(self.data)

    # GET DATA
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def getData(self):
        return self.data

    # SET DATA
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setData(self, inData):
        self.data = inData

    # GET NEXT
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def getNext(self):
        return self.next

    # SET NEXT
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setNext(self, newNext):
        self.next = newNext

    # GET PREV
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def getPrev(self):
        return self.prev

    # SET PREV
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setPrev(self, newPrev):
        self.prev = newPrev


############################################################
# 2: Linked List
############################################################
class LinkedList():

    # INIT
    def __init__(self):
        self.head = None
        self.tail = None

    # ITER
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __iter__(self):
        curNd = self.head
        while curNd is not None:
            yield curNd
            curNd = curNd.next

    # STRING
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __str__(self):
        output = ""
        for node in self:
            output = output + str(node) + ", "
        return output

    # PRINT
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def print(self):
        output = ""
        for node in self:
            output = output + " -> " + str(node)
        return output

    # SIZE
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def size(self):
        currNd = self.head
        count = 0
        while currNd:
            count += 1
            currNd = currNd.getNext()
        return count

    # FIND INDEX
    '''
    while loop with if statement to find the particular index

    idx = index

    Estimated time complexity: O(N) (best case = O(1))
    Estimated space complexity: O(1)
    '''

    def findIndex(self, idx):
        currNd = self.head
        currIdx = 0
        while (currNd != None) and (currIdx != idx):
            currIdx += 1
            currNd = currNd.getNext()
        if (currNd == None):
            raise ValueError("Index out of range!")
        else:
            node = currNd
        return node

    # IS EMPTY
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def isEmpty(self):
        currNd = self.head
        if (currNd == None):
            empty = True
        else:
            empty = False
        return empty

    # INSERT LAST
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def insertLast(self, newData):
        newNd = ListNode(newData)
        if (self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        else:
            temp = self.tail
            self.tail = newNd
            temp.setNext(newNd)
            newNd.setPrev(temp)

    # SORTED INSERT FOR EDGE INFO (Ascending exchange rates)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSorted(self, newData):
        newNd = ListNode(newData)
        current = None
        if (self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif (self.head.data.rate >= newNd.data.rate):
            temp = self.head
            self.head = newNd
            newNd.setNext(temp)
            temp.setPrev(newNd)
        else:
            current = self.head
            while (current.next != None) and (current.next.data.rate < newNd.data.rate):
                current = current.next
            if (current.next == None):
                temp = self.tail
                self.tail = newNd
                temp.setNext(newNd)
                newNd.setPrev(temp)
            else:
                temp = current.next
                current.next.setPrev(newNd)
                current.setNext(newNd)
                newNd.setNext(temp)
                newNd.setPrev(current)

    # SORTED INSERT FOR TOP VOLUME (Descending volume)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSortedTopVolume(self, newData):
        newNd = ListNode(newData)
        current = None
        if (self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif (float(self.head.data.volume) <= float(newNd.data.volume)):
            temp = self.head
            self.head = newNd
            newNd.setNext(temp)
            temp.setPrev(newNd)
        else:
            current = self.head
            while (current.next != None) and (float(current.next.data.volume) > float(newNd.data.volume)):
                current = current.next
            if (current.next == None):
                temp = self.tail
                self.tail = newNd
                temp.setNext(newNd)
                newNd.setPrev(temp)
            else:
                temp = current.next
                current.next.setPrev(newNd)
                current.setNext(newNd)
                newNd.setNext(temp)
                newNd.setPrev(current)

    # SORTED INSERT FOR TOP PRICE (Descending last price)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSortedTopPrice(self, newData):
        newNd = ListNode(newData)
        current = None
        if (self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif (float(self.head.data.lastPrice) <= float(newNd.data.lastPrice)):
            temp = self.head
            self.head = newNd
            newNd.setNext(temp)
            temp.setPrev(newNd)
        else:
            current = self.head
            while (current.next != None) and (float(current.next.data.lastPrice) > float(newNd.data.lastPrice)):
                current = current.next
            if (current.next == None):
                temp = self.tail
                self.tail = newNd
                temp.setNext(newNd)
                newNd.setPrev(temp)
            else:
                temp = current.next
                current.next.setPrev(newNd)
                current.setNext(newNd)
                newNd.setNext(temp)
                newNd.setPrev(current)

    # SORTED INSERT FOR TOP PRICE CHANGE (Descending price change in %)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSortedTopPriceChange(self, newData):
        newNd = ListNode(newData)
        current = None
        if (self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif (abs(float(self.head.data.priceChangePercent)) <= abs(float(newNd.data.priceChangePercent))):
            temp = self.head
            self.head = newNd
            newNd.setNext(temp)
            temp.setPrev(newNd)
        else:
            current = self.head
            while (current.next != None) and (abs(float(current.next.data.priceChangePercent)) > abs(float(newNd.data.priceChangePercent))):
                current = current.next
            if (current.next == None):
                temp = self.tail
                self.tail = newNd
                temp.setNext(newNd)
                newNd.setPrev(temp)
            else:
                temp = current.next
                current.next.setPrev(newNd)
                current.setNext(newNd)
                newNd.setNext(temp)
                newNd.setPrev(current)

    # SORTED INSERT FOR LOWEST SPREAD (Ascending spread in %)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSortedLowSpread(self, newData):
        newNd = ListNode(newData)
        current = None
        if float(newNd.data.spread) != 0.0:
            if (self.isEmpty() == True):
                self.head = newNd
                self.tail = newNd
            elif (float(self.head.data.spread) >= float(newNd.data.spread)):
                temp = self.head
                self.head = newNd
                newNd.setNext(temp)
                temp.setPrev(newNd)
            else:
                current = self.head
                while (current.next != None) and (float(current.next.data.spread) < float(newNd.data.spread)):
                    current = current.next
                if (current.next == None):
                    temp = self.tail
                    self.tail = newNd
                    temp.setNext(newNd)
                    newNd.setPrev(temp)
                else:
                    temp = current.next
                    current.next.setPrev(newNd)
                    current.setNext(newNd)
                    newNd.setNext(temp)
                    newNd.setPrev(current)

    # SORTED INSERT FOR HIGHEST SPREAD (Descending spread in %)
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def insertSortedHighSpread(self, newData):
        newNd = ListNode(newData)
        current = None
        if float(newNd.data.spread) > 0:
            if (self.isEmpty() == True):
                self.head = newNd
                self.tail = newNd
            elif (float(self.head.data.spread) <= float(newNd.data.spread)):
                temp = self.head
                self.head = newNd
                newNd.setNext(temp)
                temp.setPrev(newNd)
            else:
                current = self.head
                while (current.next != None) and (float(current.next.data.spread) > float(newNd.data.spread)):
                    current = current.next
                if (current.next == None):
                    temp = self.tail
                    self.tail = newNd
                    temp.setNext(newNd)
                    newNd.setPrev(temp)
                else:
                    temp = current.next
                    current.next.setPrev(newNd)
                    current.setNext(newNd)
                    newNd.setNext(temp)
                    newNd.setPrev(current)

    # REMOVE HIGH SPREAD
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def removeHighSpread(self, newData):
        newNd = ListNode(newData)
        current = None
        if float(newNd.data.data.spread) > 0:
            if (self.isEmpty() == True):
                self.head = newNd
                self.tail = newNd
            elif (float(self.head.data.data.spread) <= float(newNd.data.data.spread)):
                temp = self.head
                self.head = newNd
                newNd.setNext(temp)
                temp.setPrev(newNd)
            else:
                current = self.head
                while (current.next != None) and (float(current.next.data.data.spread) > float(newNd.data.data.spread)):
                    current = current.next
                if (current.next == None):
                    temp = self.tail
                    self.tail = newNd
                    temp.setNext(newNd)
                    newNd.setPrev(temp)
                else:
                    temp = current.next
                    current.next.setPrev(newNd)
                    current.setNext(newNd)
                    newNd.setNext(temp)
                    newNd.setPrev(current)

    # PEEK FIRST
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def peekFirst(self):
        if (self.isEmpty() == True):
            raise ValueError("List is empty!")
        else:
            nodeValue = self.head.getData()
        return nodeValue

    # PEEK LAST
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def peekLast(self):
        if (self.isEmpty() == True):
            raise ValueError("List is empty!")
        else:
            nodeValue = self.tail.getData()
        return nodeValue

    # REMOVE LAST
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def removeLast(self):
        if (self.isEmpty() == True):
            raise ValueError("List is empty!")
        elif (self.head.getNext() == None):
            self.head = None
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

    # GET NODE
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(1)
    '''

    def getNode(self, data):
        curNd = self.head
        while (curNd != None) and (curNd.getData() != data):
            curNd = curNd.getNext()
        if (curNd != None) and (curNd.getData() == data):
            node = curNd
        if (curNd == None):
            raise ValueError("Node not found...")
        return node

    # REMOVE
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(1)
    '''

    def remove(self, label):
        node = self.getNode(label)
        if node == self.head:
            self.head = self.head.getNext()
        if node == self.tail:
            self.tail = self.tail.getPrev()
        self._removeLinks(node)

    # REMOVE LINKS
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def _removeLinks(self, node):
        if node.getPrev() != None:
            node.prev.setNext(node.getNext())
        if node.getNext() != None:
            node.next.setPrev(node.getPrev())
        node.setPrev(None)
        node.setNext(None)


############################################################
# 3: Edge Info
############################################################
class EdgeInfo():

    # INIT
    def __init__(self, vertex, rate, symbol, volume):
        self.vertex = vertex
        self.rate = rate
        self.symbol = symbol
        self.volume = volume

    # STRING
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __str__(self):
        return str(self.vertex)


############################################################
# 4: Trading Pair
############################################################
class TradingPair():

    # INIT
    def __init__(self, symbol, baseAsset, quoteAsset):
        self.symbol = symbol
        self.baseAsset = baseAsset
        self.quoteAsset = quoteAsset
        self.askPrice = 0.0
        self.askQty = 0.0
        self.bidPrice = 0.0
        self.bidQty = 0.0
        self.highPrice = 0.0
        self.lowPrice = 0.0
        self.volume = 0.0
        self.openPrice = 0.0
        self.lastPrice = 0.0
        self.priceChange = 0.0
        self.priceChangePercent = ""
        self.spread = 0.0

    # STRING
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __str__(self):
        output = "######### " + self.symbol + " #########\n" + "Base Asset: " + self.baseAsset + "\nQuote Asset: " + self.quoteAsset + "\nAsk Price: " + str(self.askPrice) + "\nAsk Qty: " + str(self.askQty) + "\nBid Price: " + str(
            self.bidPrice) + "\nBid Qty: " + str(self.bidQty) + "\nHighest Price (last 24h): " + str(self.highPrice) + "\nLowest Price (last 24h): " + str(self.lowPrice) + "\nVolume (last 24h): " + str(self.volume) + "\nOpen Price (last 24h): " + str(self.openPrice) + "\nLast Price: " + str(self.lastPrice) + "\nPrice Change (last 24h): " + str(self.priceChange) + " (" + str(self.priceChangePercent) + "%)\nSpread between Ask Price and Bid Price: " + str(self.spread) + "%"
        return output

    # SET ASK PRICE
    def setAskPrice(self, askPrice):
        self.askPrice = askPrice

    # SET ASK QTY
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setAskQty(self, askQty):
        self.askQty = askQty

    # SET BID PRICE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setBidPrice(self, bidPrice):
        self.bidPrice = bidPrice

    # SET BID QTY
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setBidQty(self, bidQty):
        self.bidQty = bidQty

    # SET HIGH PRICE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setHighPrice(self, highPrice):
        self.highPrice = highPrice

    # SET LOW PRICE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setLowPrice(self, lowPrice):
        self.lowPrice = lowPrice

    # SET VOLUME
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setVolume(self, volume):
        self.volume = volume

    # SET OPEN PRICE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setOpenPrice(self, openPrice):
        self.openPrice = openPrice

    # SET LAST PRICE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setLastPrice(self, lastPrice):
        self.lastPrice = lastPrice

    # SET PRICE CHANGE
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setPriceChange(self, priceChange):
        self.priceChange = priceChange

    # SET PRICE CHANGE PERCENT
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setPriceChangePercent(self, priceChangePercent):
        self.priceChangePercent = priceChangePercent

    # SET SPREAD
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setSpread(self, askPrice, bidPrice):
        # calculates difference between askPrice and bidPrice in %
        askPrice = float(askPrice)
        bidPrice = float(bidPrice)
        if askPrice != 0 and bidPrice != 0:
            self.spread = (((askPrice - bidPrice) / askPrice)
                           * 100)
            self.spread = "%.8f" % self.spread


############################################################
# 5: Graph Vertex
############################################################
class GraphVertex():

    # INIT
    def __init__(self, label):
        self.label = label
        self.adjacents = LinkedList()
        self.visited = False

    # STRING
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def __str__(self):
        return self.label

    # PRINT
    '''
    Print function for find path

    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def print(self):
        output1 = ""
        for adjacent in self.adjacents:
            adjacent.data.rate = "%.8f" % float(adjacent.data.rate)
            output1 = output1 + "1 " + self.label + " = " + \
                str(adjacent.data.rate) + " " + str(adjacent) + " -> (" + str(adjacent.data.symbol) + ") Volume = " + \
                str(adjacent.data.volume) + "\n"
        output2 = "######### " + self.label + " #########\n" + output1
        return output2

    # GET LABEL
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def getLabel(self):
        return self.label

    # GET ADJACENT
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(1)
    '''

    def getAdjacent(self):
        return self.adjacents

    # ADD EDGE
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def addEdge(self, vertex, rate, symbol, volume):
        edgeInfo = EdgeInfo(vertex, rate, symbol, volume)
        self.adjacents.insertSorted(edgeInfo)

    # SET VISITED
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def setVisited(self):
        self.visited = True

    # CLEAR VISITED
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def clearVisited(self):
        self.visited = False

    # GET VISITED
    '''
    Estimated time complexity: O(1)
    Estimated space complexity: O(1)
    '''

    def getVisited(self):
        return self.visited


############################################################
# 6: Graph
############################################################
class Graph():

    # INIT
    def __init__(self):
        self.vertices = LinkedList()
        self.tradingPairs = LinkedList()
        # self.bestPath = stores cheapest path for self.findPath (option fast = True)
        self.bestPath = ""
        # self.bestValue = stores cheapest exchange rate for self.findPath (option fast = True)
        self.bestValue = 0.0

    # ADD VERTEX
    '''
    Add vertex to graph if vertex with same label does not exist already

    label = vertex to insert

    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def addVertex(self, label):
        newVertex = GraphVertex(label)
        if not self.hasVertex(label):
            self.vertices.insertLast(newVertex)

    # HAS VERTEX
    '''
    For loop with if statement to find the particular vertex, or not

    label = vertex to delete

    Estimated time complexity: O(N)
    Estimated space complexity: O(1)
    '''

    def hasVertex(self, label):
        result = None
        for vertex in self.vertices:
            if (label == vertex.data.getLabel()):
                result = True
        if (result == None):
            result = False
        return result

    # GET VERTEX
    '''
    For loop with if statement to find the particular vertex 

    label = vertex to find

    returns GraphVertex

    Estimated time complexity: O(N)
    Estimated space complexity: O(1)
    '''

    def getVertex(self, label):
        result = None
        for vertex in self.vertices:
            if (label == vertex.data.getLabel()):
                result = vertex
        return result

    # DELETE VERTEX
    '''
    Double for loop with if statement to remove all edges that contain the particular vertex to delete

    label = vertex to delete

    Estimated time complexity: O(N^2)
    Estimated space complexity: O(N^2)
    '''

    def delVertex(self, label):
        vToDelete = self.getVertex(label)
        for vertex in self.vertices:
            for adjacent in vertex.data.adjacents:
                if adjacent.data.vertex == vToDelete:
                    vertex.data.adjacents.remove(adjacent.data)
        self.vertices.remove(vToDelete.data)

    # ADD EDGE
    '''
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def addEdge(self, symbol, baseAsset, quoteAsset, bidPrice, askPrice, volume):
        if (bidPrice != "0.00000000") and (askPrice != "0.00000000"):
            # tradeable in both directions
            baseVertex = self.getVertex(baseAsset)
            quoteVertex = self.getVertex(quoteAsset)
            bidRate = 1 * float(bidPrice)
            askRate = 1 / float(askPrice)
            baseVertex.data.addEdge(quoteVertex, bidRate, symbol, volume)
            quoteVertex.data.addEdge(baseVertex, askRate, symbol, volume)
        elif (bidPrice == "0.00000000") and (askPrice != "0.00000000"):
            # tradeable from quote to base only
            baseVertex = self.getVertex(baseAsset)
            quoteVertex = self.getVertex(quoteAsset)
            askRate = 1 / float(askPrice)
            quoteVertex.data.addEdge(baseVertex, askRate, symbol, volume)
        elif (bidPrice != "0.00000000") and (askPrice == "0.00000000"):
            # tradeable from base to quote only
            baseVertex = self.getVertex(baseAsset)
            quoteVertex = self.getVertex(quoteAsset)
            bidRate = 1 * float(bidPrice)
            baseVertex.data.addEdge(quoteVertex, bidRate, symbol, volume)

    # DISPLAY AS LIST
    '''
    For loop to print every vertex in the graph
    
    Estimated time complexity: O(N)
    Estimated space complexity: O(N)
    '''

    def display(self):
        for vertex in self.vertices:
            print(str(vertex.data.print()))

    # FIND PATH
    '''
    Recursive algorithm to find and print all possible paths. 

    u = start vertex; 
    d = destination vertex; 
    path = empty LinkedList; 
    fast = Boolean value to calculate exchange rate or not (True = no exchange rate / False = Exchange rate)
    
    Estimated time complexity:
    fast = O(N^2)
    not fast = O(N^2)

    Estimated space complexity:
    fast = O(N)
    not fast = O(N)

    Obtained inspiration from geeksforgeeks.org, 
    https://www.geeksforgeeks.org/find-paths-given-source-destination/
    (accessed 1.10.2020)
    '''

    def findPath(self, u, d, path, fast):
        uV = self.getVertex(u)
        uV.data.setVisited()
        path.insertLast(uV.data.getLabel())
        if u == d:
            if fast == True:
                print("Start" + path.print())
            else:
                value = 1
                for i in range(path.size()-1):
                    baseV = self.getVertex(path.findIndex(i).data)
                    quoteV = self.getVertex(path.findIndex(i+1).data)
                    for i in range(self.tradingPairs.size()):
                        if self.tradingPairs.findIndex(i).data != "X":
                            if (self.tradingPairs.findIndex(i).data.baseAsset == baseV.data.getLabel()) and (self.tradingPairs.findIndex(i).data.quoteAsset == quoteV.data.getLabel()):
                                rate = 1 * \
                                    float(self.tradingPairs.findIndex(
                                        i).data.bidPrice)
                            elif (self.tradingPairs.findIndex(i).data.baseAsset == quoteV.data.getLabel()) and (self.tradingPairs.findIndex(i).data.quoteAsset == baseV.data.getLabel()):
                                rate = 1 / \
                                    float(self.tradingPairs.findIndex(
                                        i).data.askPrice)
                    if 'rate' not in locals():
                        rate = 1
                    value = float(value) * float(rate)
                    value = "%.8f" % float(value)
                print("1 " + str(path.peekFirst()) + " = " + str(value) +
                      " " + str(path.peekLast()) + ": Start" + path.print())
                if float(value) > self.bestValue:
                    self.bestValue = float(value)
                    self.bestPath = ""
                    self.bestPath = self.bestPath + "1 " + str(path.peekFirst()) + " = " + str(
                        value) + " " + str(path.peekLast()) + ": Start" + path.print()
        else:
            for adjacent in uV.data.getAdjacent():
                adjacentV = self.getVertex(str(adjacent.data.vertex))
                if (adjacentV.data.getVisited() == False):
                    self.findPath(adjacentV.data.getLabel(), d,
                                  path, fast)
        path.removeLast()
        uV.data.clearVisited()

    # FIND PATH AFTER REMOVING HIGH SPREAD
    '''
    Recursive algorithm to find and print all possible paths. 

    u = start vertex; 
    d = destination vertex; 
    path = LinkedList to store path vertices; 
    fast = Boolean value to calculate exchange rate or not (True = no exchange rate / False = Exchange rate)
    
    Estimated time complexity:
    fast = O(N^2)
    not fast = O(N^2)

    Estimated space complexity:
    fast = O(N)
    not fast = O(N)

    Obtained inspiration from geeksforgeeks.org, 
    https://www.geeksforgeeks.org/find-paths-given-source-destination/
    (accessed 1.10.2020)
    '''

    def findPath2(self, u, d, path, fast):
        uV = self.getVertex(u)
        uV.data.setVisited()
        path.insertLast(uV.data.getLabel())
        if u == d:
            if fast == True:
                print("Start" + path.print())
            else:
                value = 1
                for i in range(path.size()-1):
                    baseV = self.getVertex(path.findIndex(i).data)
                    quoteV = self.getVertex(path.findIndex(i+1).data)
                    for i in range(self.tradingPairs.size()):
                        if self.tradingPairs.findIndex(i).data != "X":
                            if (self.tradingPairs.findIndex(i).data.data.baseAsset == baseV.data.getLabel()) and (self.tradingPairs.findIndex(i).data.data.quoteAsset == quoteV.data.getLabel()):
                                rate = 1 * \
                                    float(self.tradingPairs.findIndex(
                                        i).data.data.bidPrice)
                            if (self.tradingPairs.findIndex(i).data.data.baseAsset == quoteV.data.getLabel()) and (self.tradingPairs.findIndex(i).data.data.quoteAsset == baseV.data.getLabel()):
                                rate = 1 / \
                                    float(self.tradingPairs.findIndex(
                                        i).data.data.askPrice)
                    if 'rate' not in locals():
                        rate = 1
                    value = float(value) * float(rate)
                    value = "%.8f" % float(value)
                print("1 " + str(path.peekFirst()) + " = " + str(value) +
                      " " + str(path.peekLast()) + ": Start" + path.print())
                if float(value) > self.bestValue:
                    self.bestValue = float(value)
                    self.bestPath = ""
                    self.bestPath = self.bestPath + "1 " + str(path.peekFirst()) + " = " + str(
                        value) + " " + str(path.peekLast()) + ": Start" + path.print()
        else:
            for adjacent in uV.data.getAdjacent():
                adjacentV = self.getVertex(str(adjacent.data.vertex))
                if (adjacentV.data.getVisited() == False):
                    self.findPath2(adjacentV.data.getLabel(), d,
                                   path, fast)
        path.removeLast()
        uV.data.clearVisited()
