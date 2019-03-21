#!python3
#1205_font_style_of_cells.py - Setting the Font Style of Cells

#######
#Style#
#######

#In the produce spreadsheet, for example,
#your program could apply bold text to the potato, garlic, and parsnip rows.
#Or perhaps you want to italicize every row with a cost per pound greater
#than $5. Styling parts of a large spreadsheet by hand would be tedious, but
#your programs can do it instantly.
#To customize font styles in cells, important, import the Font() and
#Style() functions from the openpyxl.styles module.

import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
# Font(size=24, italic=True) returns a Font object, which is stored in italic24Font
italic24Font = Font(size=24, italic=True)
#Set cell font to italic24Font
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello World'
wb.save('styled.xlsx')

##############
#Font Objects#
##############
#To set font style attributes, you pass keyword arguments to Font()
#Atrributes:

#Keyword argument 		Data type 		Description
#name 					String 			The font name, such as 'Calibri'or 'Times New Roman'
#size 					Integer 		The point size
#bold 					Boolean 		True, for bold font
#italic 				Boolean 		True, for italic font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pc italic'
wb.save('styles.xlsx')
