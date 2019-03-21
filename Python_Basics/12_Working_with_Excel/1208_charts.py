#! python3
#1208_charts.py - Charts


#OpenPyXL supports creating bar, line, scatter, and pie charts using the
#data in a sheet’s cells. To make a chart, you need to do the following:
#	1. Create a Reference object from a rectangular selection of cells.
#	2. Create a Series object by passing in the Reference object.
#	3. Create a Chart object.
#	4. Append the Series object to the Chart object.
#	5. Optionally, set the width and heigth
#	6. Add the Chart object to the Worksheet object with the position

#The Reference object requires some explaining. Reference objects are
#created by calling the openpyxl.chart.Reference() function and passing
#more arguments:
#	1. The Worksheet object containing your chart data.
#	2. set min_col, max_col, min_row, max_row for the data 


import openpyxl
from openpyxl.chart import BarChart, Series, Reference

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
	sheet['A' + str(i)] = i
	
refObject = openpyxl.chart.Reference(sheet, min_row=1, max_row=10, min_col=1, max_col=1)
seriesObj = openpyxl.chart.Series(refObject, title='First series')

chartObj = openpyxl.chart.BarChart()
chartObj.append(seriesObj)
chartObj.width = 15 #set the size
chartObj.height = 10

sheet.add_chart(chartObj, 'B3')
wb.save('sampleChart.xlsx')

# You can also create line charts, scatter charts, and pie charts by calling openpyxl
#.charts.LineChart(), openpyxl.charts.ScatterChart(), and openpyxl.charts
#.PieChart().

