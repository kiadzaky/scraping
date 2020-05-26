from urllib2 import urlopen
from urllib2 import Request, HTTPError
import pandas as pd

import cookielib
keyword = "xiaomi+note+7"
total= 1
nama_produk = []
harga_produk = []
gambar_produk = []
hasil=[]
for i in range(total):
    html = "https://www.jakartanotebook.com/search?key="+keyword+"&page="+str(i+1)

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = Request(html, headers=hdr)
    try:
        page = urlopen(req)
    except HTTPError, e:
        print e.fp.read()
    content = page.read()
    hasil.append(content)
    # print hasil

from bs4 import BeautifulSoup

for i in range(total):
    soup = BeautifulSoup(hasil[i], 'html.parser')
    # print (type(soup))
    # print (soup.prettify())
    produk = soup.find_all('div', attrs={'class': 'product-list'})
    for p in produk:
        gambar = p.find('img', src=True)
        nama = p.find('a', 'product-list__title').get_text().encode('utf-8')
        harga = p.find('span', 'product-list__price--coret').get_text().encode('utf-8')
        gambar_produk.append(gambar['src'])
        nama_produk.append(nama)
        harga_produk.append((int(harga.replace('Rp.', '').replace('.', ''))))
    produk_dictionary = {'gambar': gambar_produk, 'nama': nama_produk, 'harga': harga_produk}
    df = pd.DataFrame(produk_dictionary, columns=['gambar', 'nama', 'harga'])
    # print df
    df.to_csv(r'Harga_JakartaNoteBook.csv', index=False, header=True, sep=",")
