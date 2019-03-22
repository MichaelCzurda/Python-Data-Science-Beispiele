#! python3
#06_tablePrinter.py - An insecure password locker programm

table = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
	colWidths = [0] * len(tableData)
	for outter in range(len(tableData)):
		lenInner = 0
		for inner in range(len(tableData[outter])):
			maxInner=0
			lenInner += 1
			if len(tableData[outter][inner]) >= maxInner:
				maxInner=len(tableData[outter][inner])
		colWidths[outter]=maxInner+2
	
	for i in range(lenInner):
		for j in range(len(tableData)):
			print(tableData[j][i].rjust(colWidths[j]), end='')
		print()
printTable(table)
