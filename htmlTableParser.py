# Simple HtmlTableParser module
# Author: Ariff Wambeck
# Year: 2010
#opsss

import lxml.html

def parse(url, missingCell="NA"):
	"""
	Parses all HTML tables found at the given url. Missing data or those
	without text content will be replaced with the missingCell string.

	Returns a list of lists of strings, corresponding to rows within all
	found tables.
	"""
	doc = lxml.html.parse(url)
	tableList = doc.xpath("/html//table")
	dataList = []
	for table in tableList:
		dataList.append(parseTable(table, missingCell))
	return dataList

def parseTable(table, missingCell):
	"""
	Parses the individual HTML table, returning a list of its rows.
	"""
	rowList = []
	for row in table.xpath('.//tr'):
		colList = []
		cells = row.xpath('.//th') + row.xpath('.//td')
		for cell in cells:
			# The individual cell's content
			content = cell.text_content().encode("utf8")
			if content == "":
				content = missingCell
			colList.append(content)
		rowList.append(colList)
	return rowList