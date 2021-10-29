# Crypto-Graph

## Synopsis

COMP1002 Data Structures and Algorithms - Assignment


## Contents

README - README file for DSA Assignment
cryptoGraph.py - Main program to analyse binance asset data and trade data
classes.py - classes for main program cryptoGraph.py
unitTestLinkedList.py - Test harness for class: LinkedList, and related classes
unitTestGraph.py - Test harness for class: Graph, and related classes
assetData.json - Binance asset data from source https://www.binance.com/api/v3/exchangeInfo
tradeData.json - Binance trade data (last 24h) from source https://www.binance.com/api/v3/ticker/24hr


## Dependencies

README - None
cryptoGraph.py - json, pandas, matplotlib.pyplot, pickle, classes, sys
classes.py - None
unitTestLinkedList.py - json, classes
unitTestGraph.py - json, classes
assetData.json - None
tradeData.json - None


## Information on how to run programs

cryptoGraph.py - Report Mode: python3 cryptoGraph.py -r <assetdata_filename> <tradedata_filename>
                 Interactive Mode: python3 cryptoGraph.py -i

unitTestLinkedList.py - python3 unitTestLinkedList.py

unitTestGraph.py - python3 unitTestGraph.py


## Version Information

9.10.2020 - initial version of DSA Assignment programs

