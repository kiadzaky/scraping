from bs4 import BeautifulSoup
htmlText = """<img src="https://src1.com/" <img src="https://src2.com/" /> """
soup = BeautifulSoup(htmlText, 'html.parser')
print (soup.prettify())
images = soup.findAll('img')
for image in images:
    print image['src']
