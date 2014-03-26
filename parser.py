import BeautifulSoup
content_file = open('certificates.html', 'r')
content = content_file.read()
soup = BeautifulSoup.BeautifulSoup(content)
t = soup.table.tbody.findAll('tr')
f = open('certificates_formatted.txt', 'w')
for s in t:
	s = s.findAll('td')[2].a.contents[0]
	titulo = s.dd
	nomes = s.findAll('li')
	f.write(titulo.string.encode('utf-8'))
	for n in nomes:
		f.write("	" + n.string.encode('utf-8'))
	f.write('\n')
f.close()