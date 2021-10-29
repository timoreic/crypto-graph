# Student Name: Timo Reichelt
# Student ID:   19663858
# cryptoGraph.py - Main program to analyse binance asset data and trade data

""" Obtained inspiration from my previously submitted work in FOP and DSA """

############################################################
# Import modules
import json
from pandas import DataFrame
import matplotlib.pyplot as plt
import pickle
import sys
from classes import LinkedList, Graph, TradingPair


sys.setrecursionlimit(100000000)  # Increase recursion limit for serialising


############################################################
# Variables
assetDataLoaded = False
tradeDataLoaded = False
graphLoaded = False
lowSpread = False
allPairs = LinkedList()
cryptoGraph = Graph()


# ____________________________________________________________
# MAIN PROGRAM

# NO SYS.ARGV (print usage information)
if len(sys.argv) == 1:
    print("\n______________________________________________\n\nUsage:\n\nInteractive Mode: \tpython3 cryptoGraph.py -i\n\nReport Mode: \t\tpython3 cryptoGraph.py -r <asset_filename> <trade_filename>\n______________________________________________\n")

# SYS.ARGV[1] = -i (interactive mode)
elif sys.argv[1] == "-i":

    ############################################################
    # Input Menu - Start Menu
    x = None
    while x is None:
        try:
            selection = input(
                '\n######################################\nEnter selection:\n\n(1) = Load Data\n(0) = Exit\n\nYour selection... ')
            if int(selection[0]) >= 0 and int(selection[0]) <= 1:
                x = selection
            else:
                x = None
                raise ValueError()
        except:
            print('\nInvalid Input - Enter integer 0 or 1')

    ############################################################
    # Main Menu: Selection 0 - Exit
    while selection[0] != '0':

        ############################################################
        # Main Menu: Selection 1 - Load Data
        if selection[0] == '1':

            # ---------------------------------------
            # Input Menu - Load Data Menu
            y = None
            while y is None:
                try:
                    selection = input(
                        '\n######################################\nEnter selection:\n\n(1) = Load Asset Data\n(2) = Load Trade Data\n(3) = Load Serialised Data\n(4) = Load Data to Graph\n(0) = Main Menu\n\nYour selection... ')
                    if int(selection[0]) >= 0 and int(selection[0]) <= 4:
                        y = selection
                    else:
                        y = None
                        raise ValueError()
                except:
                    print('\nInvalid Input - Enter integer 0-4')

            # ---------------------------------------
            # Load Data Menu: Selection 0 - Exit
            while selection[0] != '0':

                # ---------------------------------------
                # Load Data Menu: Selection 1 - Load Asset Data
                if selection[0] == '1':
                    y = None
                    while y is None:
                        try:
                            filename = input('\nEnter File Name... ')
                            if (len(filename) < 1) or (len(filename) > 20) or (type(filename) != str):
                                y = None
                                raise ValueError()
                            else:
                                y = filename
                        except:
                            print(
                                "\nInvalid Input - File name must be a string (max 20 characters)...")

                        if filename[-5:] == ".json":
                            filename = filename
                        else:
                            filename = filename + ".json"

                    print("\nLoading Asset data...")
                    try:
                        with open(filename, 'r') as f:
                            # datastore1 = dictionary
                            datastore1 = json.load(f)
                    except:
                        print("\nAsset data could not be loaded...")

                    # Add asset data to LinkedList (allPairs)
                    '''
                    For loop iterates through all dictionaries in list "symbols" of the dictionary "datastore1".

                    allPairs = LinkedList to store asset data (symbol; baseAssset; quoteAsset)

                    Estimated time complexity: O(N)
                    Estimated space complexity: O(N)
                    '''
                    allPairs = LinkedList()
                    for i in range(len(datastore1["symbols"])):
                        allPairs.insertLast(TradingPair(
                            datastore1["symbols"][i]["symbol"], datastore1["symbols"][i]["baseAsset"], datastore1["symbols"][i]["quoteAsset"]))

                    print("\nAsset data loaded!")
                    assetDataLoaded = True

                # ---------------------------------------
                # Load Data Menu: Selection 2 - Load Trade Data
                elif selection[0] == '2':
                    y = None
                    while y is None:
                        try:
                            filename = input('\nEnter File Name... ')
                            if (len(filename) < 1) or (len(filename) > 20) or (type(filename) != str):
                                y = None
                                raise ValueError()
                            else:
                                y = filename
                        except:
                            print(
                                "\nInvalid Input - File name must be a string (max 20 characters)...")

                        if filename[-5:] == ".json":
                            filename = filename
                        else:
                            filename = filename + ".json"

                    print("\nLoading Trade data...")
                    try:
                        with open(filename, 'r') as f:
                            # datastore2 = list
                            datastore2 = json.load(f)
                    except:
                        print("\nTrade data could not be loaded...")

                    # Add trade data to Linked List (allPairs)
                    '''
                    Double for loop iterates through all pairs in linked list "allPairs", and through all dictionaries in list "datastore2".
                    If statement to match and combine asset information with tradepair information (bidPrice; askPrice; highPrice; lowPrice; openPrice; lastPrice; priceChange; priceChangePercent; spread)

                    allPairs = LinkedList to store asset data and trade data (symbol; baseAssset; quoteAsset; bidPrice; askPrice; highPrice; lowPrice; openPrice; lastPrice; priceChange; priceChangePercent; spread)

                    Estimated time complexity: O(N^2)
                    Estimated space complexity: O(N)
                    '''
                    for i in range(len(datastore2)):
                        for pair in allPairs:
                            if pair.data.symbol == datastore2[i]["symbol"]:
                                pair.data.setBidPrice(
                                    datastore2[i]["bidPrice"])
                                pair.data.setBidQty(datastore2[i]["bidQty"])
                                pair.data.setAskPrice(
                                    datastore2[i]["askPrice"])
                                pair.data.setAskQty(datastore2[i]["askQty"])
                                pair.data.setHighPrice(
                                    datastore2[i]["highPrice"])
                                pair.data.setLowPrice(
                                    datastore2[i]["lowPrice"])
                                pair.data.setVolume(datastore2[i]["volume"])
                                pair.data.setOpenPrice(
                                    datastore2[i]["openPrice"])
                                pair.data.setLastPrice(
                                    datastore2[i]["lastPrice"])
                                pair.data.setPriceChange(
                                    datastore2[i]["priceChange"])
                                pair.data.setPriceChangePercent(
                                    datastore2[i]["priceChangePercent"])
                                pair.data.setSpread(
                                    datastore2[i]["askPrice"], datastore2[i]["bidPrice"])

                    tradeDataLoaded = True
                    print("\nTrade data loaded!")

                # ---------------------------------------
                # Load Data Menu: Selection 3 - Load Serialised Data
                elif selection[0] == '3':
                    y = None
                    while y is None:
                        try:
                            filename = input('\nEnter File Name... ')
                            if (len(filename) < 1) or (len(filename) > 20) or (type(filename) != str):
                                y = None
                                raise ValueError()
                            else:
                                y = filename
                        except:
                            print(
                                "\nInvalid Input - File name must be a string (max 20 characters)...")

                        if filename[-4:] == ".csv":
                            filename = filename
                        else:
                            filename = filename + ".csv"

                    try:
                        print("\nLoading serialized file...")
                        with open(filename, "rb") as dataFile:
                            cryptoGraph = pickle.load(dataFile)
                            print("Loaded Object from File!")
                    except:
                        print("Error: Problem pickling Object!")

                    graphLoaded = True

                    # for loop with if statement to check if low spread or not
                    '''
                    Estimated time complexity: O(N)
                    Estimated space complexity: O(1)
                    '''
                    x = 0
                    tradingPairLength = cryptoGraph.tradingPairs.size()
                    for pair in cryptoGraph.tradingPairs:
                        if pair.data == "X":
                            x += 1

                    length = int(round((tradingPairLength // 2) - 1))
                    if x >= length:
                        lowSpread = True
                    print("Graph loaded and lowSpread = " + str(lowSpread))

                # ---------------------------------------
                # Load Data Menu: Selection 4 - Load Data to Graph (cryptoGraph)
                # Estimated Time complexity = O(N)
                # Estimated Space complexity = O(N)
                elif selection[0] == '4':
                    cryptoGraph = Graph()
                    print("\nLoading data to graph...")
                    if (not tradeDataLoaded) or (not assetDataLoaded):
                        print("\n###### ERROR LOADING DATA ######\nTo load data to graph follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
                    else:
                        cryptoGraph.tradingPairs = allPairs
                        for i in range(cryptoGraph.tradingPairs.size()):
                            # add vertices
                            cryptoGraph.addVertex(
                                cryptoGraph.tradingPairs.findIndex(i).data.quoteAsset)
                            cryptoGraph.addVertex(
                                cryptoGraph.tradingPairs.findIndex(i).data.baseAsset)
                            # add edges
                            cryptoGraph.addEdge(cryptoGraph.tradingPairs.findIndex(i).data.symbol, cryptoGraph.tradingPairs.findIndex(i).data.baseAsset, cryptoGraph.tradingPairs.findIndex(
                                i).data.quoteAsset, cryptoGraph.tradingPairs.findIndex(i).data.bidPrice, allPairs.findIndex(i).data.askPrice, cryptoGraph.tradingPairs.findIndex(i).data.volume)
                        graphLoaded = True
                        print("\nData loaded to graph!")

                # ---------------------------------------
                # Input Menu (In Loop): Load Data Menu
                y = None
                while y is None:
                    try:
                        selection = input(
                            '\n######################################\nEnter selection:\n\n(1) = Load Asset Data\n(2) = Load Trade Data\n(3) = Load Serialised Data\n(4) = Load Data to Graph\n(0) = Main Menu\n\nYour selection... ')
                        if int(selection[0]) >= 0 and int(selection[0]) <= 4:
                            y = selection
                        else:
                            y = None
                            raise ValueError()
                    except:
                        print('\nInvalid Input - Enter integer 0-4')

        ############################################################
        # Main Menu: Selection 2 - Find and Display Asset
        # Estimated Time complexity = O(N)
        # Estimated Space complexity = O(1)
        elif selection[0] == '2':

            if ((not graphLoaded)):
                print("\n###### ERROR ######\nTo find and display assets load serialised file, or follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            # ---------------------------------------
            # Input: Asset
            else:
                y = None
                while y is None:
                    try:
                        asset = input(
                            '\nEnter Asset Name... ')
                        if (len(asset) < 3) or (len(asset) > 6) or (type(asset) != str):
                            y = None
                            raise ValueError()
                        else:
                            y = asset
                    except:
                        print(
                            '\nInvalid Input - Asset name must be a string with 3-6 characters...')

                    try:
                        asset = cryptoGraph.getVertex(asset.upper())
                        if asset is None:
                            y = None
                            raise ValueError()
                        else:
                            y = asset
                    except:
                        print("\nInvalid Input - Vertex not found...")

                print(asset.data.print())

        ############################################################
        # Main Menu: Selection 3 - Find and Display Trade Details
        # Estimated Time complexity = O(N)
        # Estimated Space complexity = O(1)
        elif selection[0] == '3':
            if (not graphLoaded):
                print("\n###### ERROR ######\nTo find and display trade pairs follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                # ---------------------------------------
                # Input: Trade Pair
                y = None
                while y is None:
                    try:
                        symbol = input('\nEnter Trade Pair Name...')
                        if (len(symbol) < 5) or (len(symbol) > 12) or (type(symbol) != str):
                            y = None
                            raise ValueError()
                        else:
                            y = symbol
                            symbol = symbol.upper()
                    except:
                        print(
                            '\nInvalid Input - Trade Pair Name must be a string with 3-6 characters...')

                    if not lowSpread:
                        try:
                            pairFound = False
                            for i in range(cryptoGraph.tradingPairs.size()):
                                if cryptoGraph.tradingPairs.findIndex(i).data != "X":
                                    if cryptoGraph.tradingPairs.findIndex(i).data.symbol == symbol:
                                        symbol = cryptoGraph.tradingPairs.findIndex(
                                            i).data
                                        pairFound = True

                            if pairFound:
                                y = symbol
                            else:
                                y = None
                                raise ValueError()
                        except:
                            print("\nInvalid Input - Trade Pair not found...")
                    else:
                        try:
                            pairFound = False
                            for i in range(cryptoGraph.tradingPairs.size()):
                                if cryptoGraph.tradingPairs.findIndex(i).data != "X":
                                    if cryptoGraph.tradingPairs.findIndex(i).data.data.symbol == symbol:
                                        symbol = cryptoGraph.tradingPairs.findIndex(
                                            i).data.data
                                        pairFound = True

                            if pairFound:
                                y = symbol
                            else:
                                y = None
                                raise ValueError()
                        except:
                            print("\nInvalid Input - Trade Pair not found...")

                print("\n" + str(symbol))

        ############################################################
        # Main Menu: Selection 4 - Find and Display Trade Paths
        elif selection[0] == '4':
            if (not graphLoaded):
                print("\n###### ERROR ######\nTo find and display trade paths follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                # ---------------------------------------
                # Input: Asset1
                y = None
                while y is None:
                    try:
                        asset1 = input('\nEnter Start Asset Name... ')
                        if (len(asset1) < 3) or (len(asset1) > 6) or (type(asset1) != str):
                            y = None
                            raise ValueError()
                        else:
                            y = asset1
                    except:
                        print(
                            '\nInvalid Input - Asset name must be a string with 3-6 characters...')

                    try:
                        asset1 = cryptoGraph.getVertex(asset1.upper())
                        if asset1 is None:
                            y = None
                            raise ValueError()
                        else:
                            y = asset1
                    except:
                        print("\nInvalid Input - Vertex not found...")

                # ---------------------------------------
                # Input: Asset2
                z = None
                while z is None:
                    try:
                        asset2 = input(
                            '\nEnter End Asset Name... ')
                        if (len(asset2) < 3) or (len(asset2) > 6) or (type(asset2) != str):
                            z = None
                            raise ValueError()
                        else:
                            z = asset2
                    except:
                        print(
                            '\nInvalid Input - Asset name must be a string with 3-6 characters...')

                    try:
                        asset2 = cryptoGraph.getVertex(asset2.upper())
                        if asset2 is None:
                            z = None
                            raise ValueError()
                        else:
                            z = asset2
                    except:
                        print("\nInvalid Input - Vertex not found...")

                # ---------------------------------------
                # Input Menu - Find Path Menu
                f = None
                while f is None:
                    try:
                        selection = input(
                            '\n######################################\nEnter selection:\n\n(1) = Find possible paths (fast)\n(2) = Find possible paths including price (slow)\n\nYour selection... ')
                        if int(selection[0]) > 0 and int(selection[0]) <= 2:
                            f = selection[0]
                        else:
                            f = None
                            raise ValueError()
                    except:
                        print('\nInvalid Input - Enter integer 1 or 2')

                if f == "1":
                    fast = True
                else:
                    fast = False

                path = LinkedList()
                if not lowSpread:
                    print(cryptoGraph.findPath(
                        str(asset1), str(asset2), path, fast))
                    if (not fast):
                        print("\n********************************************************************************\n\nCheapest Path: " +
                              cryptoGraph.bestPath + "\n\n********************************************************************************")
                else:
                    print(cryptoGraph.findPath2(
                        str(asset1), str(asset2), path, fast))
                    if (not fast):
                        print("\n********************************************************************************\n\nCheapest Path: " +
                              cryptoGraph.bestPath + "\n\n********************************************************************************")

        ############################################################
        # Main Menu: Selection 5 - Set Asset Filter
        elif selection[0] == '5':
            if (not graphLoaded):
                print("\n###### ERROR ######\nTo set asset filters follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                # ---------------------------------------
                # Input Menu - Set Asset Filter Menu
                y = None
                while y is None:
                    try:
                        selection = input(
                            '\n######################################\nEnter selection:\n\n(1) = Remove Asset\n(2) = Remove Trade Pairs with High Spread\n(0) = Main Menu\n\nYour selection... ')
                        if int(selection[0]) >= 0 and int(selection[0]) <= 2:
                            y = selection
                        else:
                            y = None
                            raise ValueError()
                    except:
                        print('\nInvalid Input - Enter integer 0-2')

                # ---------------------------------------
                # Set Asset Filter Menu: Selection 0 - Exit
                while selection[0] != '0':

                    # ---------------------------------------
                    # Set Asset Filter Menu: Selection 1 - Remove Asset
                    if selection[0] == '1':

                        # ---------------------------------------
                        # Input: Asset
                        y = None
                        while y is None:
                            try:
                                asset = input(
                                    '\nEnter Asset Name to Remove... ')
                                if (len(asset) < 3) or (len(asset) > 6) or (type(asset) != str):
                                    y = None
                                    raise ValueError()
                                else:
                                    y = asset
                            except:
                                print(
                                    '\nInvalid Input - Asset name must be a string with 3-6 characters...')

                            try:
                                asset = cryptoGraph.getVertex(asset.upper())
                                if asset is None:
                                    y = None
                                    raise ValueError()
                                else:
                                    y = asset
                            except:
                                print("\nInvalid Input - Vertex not found...")

                        # Remove Edges
                        # Estimated Time complexity = O(N^2)
                        # Estimated Space complexity = O(1)
                        for vertex in cryptoGraph.vertices:
                            for adjacent in vertex.data.adjacents:
                                if str(adjacent.data.vertex) == str(asset):
                                    vertex.data.adjacents.remove(adjacent.data)

                        # Remove Vertex
                        asset = cryptoGraph.getVertex(str(asset))
                        cryptoGraph.vertices.remove(asset.data)

                        # Remove Trade Pairs
                        # Estimated Time complexity = O(N)
                        # Estimated Space complexity = O(1)
                        if not lowSpread:
                            for i in range(cryptoGraph.tradingPairs.size()):
                                if cryptoGraph.tradingPairs.findIndex(i).data != "X":
                                    if cryptoGraph.tradingPairs.findIndex(i).data.quoteAsset == str(asset) or cryptoGraph.tradingPairs.findIndex(i).data.baseAsset == str(asset):
                                        cryptoGraph.tradingPairs.findIndex(
                                            i).data = "X"

                        else:
                            for i in range(cryptoGraph.tradingPairs.size()):
                                if cryptoGraph.tradingPairs.findIndex(i).data != "X":
                                    if cryptoGraph.tradingPairs.findIndex(i).data.data.quoteAsset == str(asset) or cryptoGraph.tradingPairs.findIndex(i).data.data.baseAsset == str(asset):
                                        cryptoGraph.tradingPairs.findIndex(
                                            i).data = "X"

                        print("\n" + str(asset) + " removed!")

                    # ---------------------------------------
                    # Set Asset Filter Menu: Selection 2 - Remove Trade Pairs with High Spread
                    # Estimated Time complexity = O(N)
                    # Estimated Space complexity = O(N)
                    if selection[0] == '2':

                        if lowSpread:
                            print("\nTrade Pairs with high spread already removed!")
                        else:
                            highestSpread = LinkedList()

                            for pair in cryptoGraph.tradingPairs:
                                if (pair.data != "X") and (pair.data.askPrice != 0.0) and (pair.data.bidPrice != 0.0):
                                    highestSpread.removeHighSpread(pair)

                            for i in range(round(highestSpread.size()/2)):
                                highestSpread.findIndex(i).data = "X"

                            # Add vertices to low spread graph
                            cryptoGraph = Graph()
                            for pair in highestSpread:
                                if pair.data != "X":
                                    cryptoGraph.addVertex(
                                        pair.data.data.quoteAsset)
                                    cryptoGraph.addVertex(
                                        pair.data.data.baseAsset)

                            # Add edges to low spread graph
                            for i in range(highestSpread.size()):
                                if highestSpread.findIndex(i).data != "X":
                                    cryptoGraph.addEdge(highestSpread.findIndex(i).data.data.symbol, highestSpread.findIndex(i).data.data.baseAsset, highestSpread.findIndex(
                                        i).data.data.quoteAsset, highestSpread.findIndex(i).data.data.bidPrice, highestSpread.findIndex(i).data.data.askPrice, highestSpread.findIndex(i).data.data.volume)

                            allPairs = highestSpread
                            cryptoGraph.tradingPairs = allPairs
                            lowSpread = True

                            print("\nTrade Pairs with high spread removed!")

                    # ---------------------------------------
                    # Input Menu (In Loop) - Set Asset Filter Menu
                    y = None
                    while y is None:
                        try:
                            selection = input(
                                '\n######################################\nEnter selection:\n\n(1) = Remove Asset\n(2) = Remove Trade Pairs with High Spread\n(0) = Main Menu\n\nYour selection... ')
                            if int(selection[0]) >= 0 and int(selection[0]) <= 2:
                                y = selection
                            else:
                                y = None
                                raise ValueError()
                        except:
                            print('\nInvalid Input - Enter integer 0-2')

        ############################################################
        # Main Menu: Selection 6 - Asset Overview
        # Estimated time complexity: O(N)
        # Estimated space complexity: O(1)
        elif selection[0] == '6':
            if (not graphLoaded):
                print("\n###### ERROR ######\nTo see asset overview upload serialised file, or follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                print(cryptoGraph.display())

        ############################################################
        # Main Menu: Selection 7 - Trade Overview
        # Estimated time complexity: O(N)
        # Estimated space complexity: O(N)
        elif selection[0] == '7':

            if (not graphLoaded):
                print("\n###### ERROR ######\nTo see trade overview follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                if not lowSpread:
                    topVolume = LinkedList()
                    topPrice = LinkedList()
                    topPriceChange = LinkedList()
                    lowestSpread = LinkedList()
                    highestSpread = LinkedList()

                    for pair in cryptoGraph.tradingPairs:
                        if pair.data != "X":
                            topVolume.insertSortedTopVolume(pair.data)
                            topPrice.insertSortedTopPrice(pair.data)
                            topPriceChange.insertSortedTopPriceChange(
                                pair.data)
                            lowestSpread.insertSortedLowSpread(pair.data)
                            highestSpread.insertSortedHighSpread(pair.data)
                else:
                    topVolume = LinkedList()
                    topPrice = LinkedList()
                    topPriceChange = LinkedList()
                    lowestSpread = LinkedList()
                    highestSpread = LinkedList()

                    for pair in cryptoGraph.tradingPairs:
                        if pair.data != "X":
                            topVolume.insertSortedTopVolume(pair.data.data)
                            topPrice.insertSortedTopPrice(pair.data.data)
                            topPriceChange.insertSortedTopPriceChange(
                                pair.data.data)
                            lowestSpread.insertSortedLowSpread(pair.data.data)
                            highestSpread.insertSortedHighSpread(
                                pair.data.data)

                # ---------------------------------------
                # Input Menu - Trade Overview Menu
                y = None
                while y is None:
                    try:
                        selection = input(
                            '\n######################################\nEnter selection:\n\n(1) = Top 10 Volume\n(2) = Top 10 Price\n(3) = Top 10 Price Change\n(4) = Top 10 Lowest Spread\n(5) = Top 10 Highest Spread\n(6) = Top 3 Highest Volume Pie Chart\n(0) = Main Menu\n\nYour selection... ')
                        if int(selection[0]) >= 0 and int(selection[0]) <= 6:
                            y = selection
                        else:
                            y = None
                            raise ValueError()
                    except:
                        print('\nInvalid Input - Enter integer 0-6')

                # ---------------------------------------
                # Trade Overview Menu: Selection 0 - Exit
                while selection[0] != '0':

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 1 - Top 10 Volume
                    if selection[0] == '1':
                        print("\n################## TOP 10 VOLUME ##################")
                        i = 0
                        while i < 10:
                            print("\n------------ " + str(i+1) + " ------------\n" +
                                  str(topVolume.findIndex(i)))
                            i += 1

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 2 - Top 10 Price
                    if selection[0] == '2':
                        print("\n################## TOP 10 PRICE ##################")
                        i = 0
                        while i < 10:
                            print("\n------------ " + str(i+1) + " ------------\n" +
                                  str(topPrice.findIndex(i)))
                            i += 1

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 3 - Top 10 Price Change
                    if selection[0] == '3':
                        print(
                            "\n################## TOP 10 PRICE CHANGE ##################")
                        i = 0
                        while i < 10:
                            print("\n------------ " + str(i+1) + " ------------\n" +
                                  str(topPriceChange.findIndex(i)))
                            i += 1

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 4 - Top 10 Lowest Spread
                    if selection[0] == '4':
                        print(
                            "\n################## TOP 10 LOWEST SPREAD ##################")
                        i = 0
                        while i < 10:
                            print("\n------------ " + str(i+1) + " ------------\n" +
                                  str(lowestSpread.findIndex(i)))
                            i += 1

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 5 - Top 10 Highest Spread
                    if selection[0] == '5':
                        print(
                            "\n################## TOP 10 HIGHEST SPREAD ##################")
                        i = 0
                        while (i < 10):
                            print("\n------------ " + str(i+1) + " ------------\n" +
                                  str(highestSpread.findIndex(i)))
                            i += 1

                    # ---------------------------------------
                    # Trade Overview Menu: Selection 6 - Top 3 Highest Volume Pie Chart
                    if selection[0] == '6':
                        one = float(topVolume.findIndex(0).data.volume)
                        two = float(topVolume.findIndex(1).data.volume)
                        three = float(topVolume.findIndex(2).data.volume)
                        Data = {'Volume': [one, two, three]}
                        df = DataFrame(Data, columns=['Volume'], index=[
                            topVolume.findIndex(0).data.symbol, topVolume.findIndex(1).data.symbol, topVolume.findIndex(2).data.symbol])

                        df.plot.pie(y='Volume', figsize=(5, 5),
                                    autopct='%1.1f%%', startangle=90)
                        plt.show()

                    # ---------------------------------------
                    # Input Menu (In Loop) - Trade Overview Menu
                    y = None
                    while y is None:
                        try:
                            selection = input(
                                '\n######################################\nEnter selection:\n\n(1) = Top 10 Volume\n(2) = Top 10 Price\n(3) = Top 10 Price Change\n(4) = Top 10 Lowest Spread\n(5) = Top 10 Highest Spread\n(6) = Top 3 Highest Volume Pie Chart\n(0) = Main Menu\n\nYour selection... ')
                            if int(selection[0]) >= 0 and int(selection[0]) <= 6:
                                y = selection
                            else:
                                y = None
                                raise ValueError()
                        except:
                            print('\nInvalid Input - Enter integer 0-6')

        ############################################################
        # Main Menu: Selection 8 - Save data (serialised)
        # Estimated time complexity: O(N)
        # Estimated space complexity: O(N)
        elif selection[0] == '8':
            if not graphLoaded:
                print("\n###### ERROR ######\nGraph does not exist. To create a Graph follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
            else:
                y = None
                while y is None:
                    try:
                        name = input('\nEnter File Name... ')
                        if (len(name) < 1) or (len(name) > 20) or (type(name) != str):
                            y = None
                            raise ValueError()
                        else:
                            y = name
                    except:
                        print(
                            '\nInvalid Input - File name must be a string (max 20 characters)...')

                if name[-4:] == ".csv":
                    name = name[0:-4]
                else:
                    name = name

                try:
                    with open(str(name) + ".csv", "wb") as dataFile:
                        pickle.dump(cryptoGraph, dataFile)
                        print("Saved Object to File!")
                except:
                    print("Error: Problem pickling Object!")

        ############################################################
        # Input Menu (In Loop): Main Menu
        x = None
        while x is None:
            try:
                selection = input('\n######################################\nEnter selection:\n\n(1) = Load Data\n(2) = Find and Display Asset\n(3) = Find and Display Trade Details\n(4) = Find and Display Trade Paths\n(5) = Set Asset Filter\n(6) = Asset Overview\n(7) = Trade Overview\n(8) = Save Data (serialised)\n(0) = Exit\n\nYour selection... ')
                if int(selection[0]) >= 0 and int(selection[0]) <= 8:
                    x = selection
                else:
                    x = None
                    raise ValueError()
            except:
                print('\nInvalid Input - Enter integer 0-8')

# SYS.ARGV[1] + asset data + trade data = -r (report mode)
elif (sys.argv[1] == "-r") and (len(sys.argv) == 4):

    # _____________________________________________
    # Load Asset Data
    print("\nLoading Asset data...")
    try:
        with open(sys.argv[2], 'r') as f:
            datastore1 = json.load(f)
    except:
        print("\nAsset data could not be loaded...\n")

    # Add asset data to allPairs
    allPairs = LinkedList()
    for i in range(len(datastore1["symbols"])):
        allPairs.insertLast(TradingPair(
            datastore1["symbols"][i]["symbol"], datastore1["symbols"][i]["baseAsset"], datastore1["symbols"][i]["quoteAsset"]))

    print("Asset data loaded!")
    assetDataLoaded = True

    # _____________________________________________
    # Load Trade Data
    print("\nLoading Trade data...")
    try:
        with open(sys.argv[3], 'r') as f:
            datastore2 = json.load(f)
    except:
        print("\nTrade data could not be loaded...\n")

    # Add trade data to allPairs
    for i in range(len(datastore2)):
        for pair in allPairs:
            if pair.data.symbol == datastore2[i]["symbol"]:
                pair.data.setBidPrice(
                    datastore2[i]["bidPrice"])
                pair.data.setBidQty(datastore2[i]["bidQty"])
                pair.data.setAskPrice(
                    datastore2[i]["askPrice"])
                pair.data.setAskQty(datastore2[i]["askQty"])
                pair.data.setHighPrice(
                    datastore2[i]["highPrice"])
                pair.data.setLowPrice(
                    datastore2[i]["lowPrice"])
                pair.data.setVolume(datastore2[i]["volume"])
                pair.data.setOpenPrice(
                    datastore2[i]["openPrice"])
                pair.data.setLastPrice(
                    datastore2[i]["lastPrice"])
                pair.data.setPriceChange(
                    datastore2[i]["priceChange"])
                pair.data.setPriceChangePercent(
                    datastore2[i]["priceChangePercent"])
                pair.data.setSpread(
                    datastore2[i]["askPrice"], datastore2[i]["bidPrice"])

    tradeDataLoaded = True
    print("Trade data loaded!")

    # _____________________________________________
    # Load Asset / Trade Data to Graph
    cryptoGraph = Graph()
    print("\nLoading data to graph...")
    if ((not assetDataLoaded) or (not tradeDataLoaded)):
        print("\n###### ERROR LOADING DATA ######\nTo load data to graph follow these steps:\n\nFirst: Load Asset Data\nSecond: Load Trade Data\nThird: Load Data to Graph")
    else:
        for i in range(allPairs.size()):
            if (allPairs.findIndex(i).data.bidPrice != "0.00000000") and (allPairs.findIndex(i).data.askPrice != "0.00000000"):
                cryptoGraph.addVertex(
                    allPairs.findIndex(i).data.quoteAsset)
                cryptoGraph.addVertex(
                    allPairs.findIndex(i).data.baseAsset)
                cryptoGraph.addEdge(allPairs.findIndex(i).data.symbol, allPairs.findIndex(i).data.baseAsset, allPairs.findIndex(
                    i).data.quoteAsset, allPairs.findIndex(i).data.bidPrice, allPairs.findIndex(i).data.askPrice, allPairs.findIndex(i).data.volume)
        graphLoaded = True
        print("Data loaded to graph!")

    # _____________________________________________
    # Asset Overview
    print(cryptoGraph.display())

    # _____________________________________________
    # Trade Overview
    topVolume = LinkedList()
    topPrice = LinkedList()
    topPriceChange = LinkedList()
    lowestSpread = LinkedList()
    highestSpread = LinkedList()

    for pair in allPairs:
        if pair.data != "X":
            topVolume.insertSortedTopVolume(pair.data)
            topPrice.insertSortedTopPrice(pair.data)
            topPriceChange.insertSortedTopPriceChange(
                pair.data)
            lowestSpread.insertSortedLowSpread(pair.data)
            highestSpread.insertSortedHighSpread(pair.data)

    # _____________________________________________
    # Top 10 Volume
    print("\n################## TOP 10 VOLUME ##################")
    i = 0
    while i < 10:
        print("\n------------ " + str(i+1) + " ------------\n" +
              str(topVolume.findIndex(i)))
        i += 1

    # _____________________________________________
    # Top 10 Price
    print("\n################## TOP 10 PRICE ##################")
    i = 0
    while i < 10:
        print("\n------------ " + str(i+1) + " ------------\n" +
              str(topPrice.findIndex(i)))
        i += 1

    # _____________________________________________
    # Top 10 Price Change
    print(
        "\n################## TOP 10 PRICE CHANGE ##################")
    i = 0
    while i < 10:
        print("\n------------ " + str(i+1) + " ------------\n" +
              str(topPriceChange.findIndex(i)))
        i += 1

    # _____________________________________________
    # Top 10 Lowest Spread
    print(
        "\n################## TOP 10 LOWEST SPREAD ##################")
    i = 0
    while i < 10:
        print("\n------------ " + str(i+1) + " ------------\n" +
              str(lowestSpread.findIndex(i)))
        i += 1

    # _____________________________________________
    # Top 10 Highest Spread
    print(
        "\n################## TOP 10 HIGHEST SPREAD ##################")
    i = 0
    while (i < 10):
        print("\n------------ " + str(i+1) + " ------------\n" +
              str(highestSpread.findIndex(i)))
        i += 1

    # _____________________________________________
    # Top 3 Highest Volume Pie Chart
    one = float(topVolume.findIndex(0).data.volume)
    two = float(topVolume.findIndex(1).data.volume)
    three = float(topVolume.findIndex(2).data.volume)
    Data = {'Volume': [one, two, three]}
    df = DataFrame(Data, columns=['Volume'], index=[
        topVolume.findIndex(0).data.symbol, topVolume.findIndex(1).data.symbol, topVolume.findIndex(2).data.symbol])

    df.plot.pie(y='Volume', figsize=(5, 5),
                autopct='%1.1f%%', startangle=90)
    plt.show()

# SYS.ARGV ELSE (print usage)
else:
    print("\n______________________________________________\n\nUsage:\n\nInteractive Mode: \tpython3 cryptoGraph.py -i\n\nReport Mode: \t\tpython3 cryptoGraph.py -r <asset_filename> <trade_filename>\n______________________________________________\n")
