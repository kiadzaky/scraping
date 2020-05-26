from urllib2 import urlopen
from urllib2 import Request, HTTPError
import pandas as pd
from bs4 import BeautifulSoup

def pencarian_berita():
    total = 1
    nama_produk = []
    harga_produk = []
    url_array = []
    df_array= []
    hasil = []
    html = "https://www.antaranews.com/terkini"

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
    # print content
    soup = BeautifulSoup(content, 'html.parser')
    # print (type(soup))
    # print (soup.prettify())
    produk = soup.find_all('article', attrs={'class': 'simple-post simple-big clearfix'})
    for p in produk:
        link = p.find('a', href=True)
        url_array.append(link['href'])
    produk_dictionary = {'link': url_array}
    df = pd.DataFrame(produk_dictionary, columns=['link'])
    df_array.append(df)
    df.to_json('antara.json')
pencarian_berita()