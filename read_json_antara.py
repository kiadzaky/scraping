import json
from urllib2 import urlopen
from urllib2 import Request, HTTPError
import pandas as pd
from bs4 import BeautifulSoup

url_array =[]
hasil =[]
judul_array = []
tanggal_array = []
gambar_array = []
caption_array = []
konten_array = []

with open('antara.json') as json_file:
    data = json.load(json_file)
    for p in data['link']:
        url = data['link'][p]
        url_array.append(url)
    # print url_array
for i in url_array:
    html = i

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
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
    # with open('text.txt','w') as outfile:
    #     json.dump(hasil,outfile)

for i in hasil:
    soup = BeautifulSoup(hasil[int(i)], 'html.parser')
    produk = soup.find_all('article', attrs={'class': 'post-wrapper clearfix'})
    for p in produk:
        judul = p.find('h1', 'post-title').get_text()
        tanggal = p.find('p', 'simple-share').get_text()
        gambar = p.find('source', srcset=True)
        caption = p.find('div', 'wp-caption')
        konten = p.find('div', 'post-content clearfix')

        judul_array.append(judul)
        tanggal_array.append(tanggal)
        gambar_array.append(gambar)
        caption_array.append(caption)
        konten_array.append(konten)
        produk_dictionary = {'judul' : judul_array, 'tanggal': tanggal_array, 'gambar': gambar_array
            , 'caption': caption_array, 'konten': konten_array}
        df = pd.DataFrame(produk_dictionary, columns=['judul','tanggal','gambar','caption','konten'])
        df.to_csv("Antara_json.json",sep=',')