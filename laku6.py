from urllib2 import urlopen
keyword = "xiaomi"
html = urlopen("https://www.laku6.com/jual/hp-bekas-bergaransi-search?term="+keyword).read()
# print html
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
# print (type(soup))
# print (soup.prettify())


import pandas as pd
gambar_produk = []
nama_produk = []
harga_produk = []
produk = soup.find_all('div', attrs={'class': 'col-xs-3 big-list-item'})
for p in produk:
        gambar = p.find('img', src=True)
        nama = p.find('span', 'post-display-name').get_text().encode('utf-8')
        harga = p.find('span', 'selling-price usual').get_text().encode('utf-8')
        gambar_produk.append(gambar['src'])
        nama_produk.append(nama)
        harga_produk.append((int(harga.replace('Rp.', '').replace(',', ''))))
produk_dictionary = {'gambar': gambar_produk, 'nama': nama_produk, 'harga': harga_produk}
df = pd.DataFrame(produk_dictionary, columns=['gambar', 'nama', 'harga'])
# print df
df.to_csv(r'Harga.csv', index=False, header=True, sep=",")
