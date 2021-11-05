import requests
from bs4 import BeautifulSoup, NavigableString
import urllib3
import threading
from base64 import b64encode
#from .BaseController import BaseController
import logging
logging.basicConfig(filename='./scrapping-ej.log', level=logging.DEBUG)

class Scrapper(object):
    def __init__(self, url, proxy):
        self.url = url
        self.proxy = proxy
        self.pos = 0
        self.currurl = ''
        self.lista = []
        
        if(self.proxy):
            self.http = urllib3.ProxyManager(self.proxy)
        else:
            self.http = urllib3.PoolManager()
    
    def make_url_base(self):
        self.currurl = self.url.format('/places/default/index/{}'.format(self.pos))
        self.pos += 1
        return True
    
    def extract_currurl(self):
        while True:
            self.make_url_base()
            if(self.extract_currurl_base()):
                break

    def extract_currurl_base(self):
        web = self.http.request('GET',self.currurl)
        soup = BeautifulSoup(web.data, 'lxml')
        img = soup.find_all('img')
        if(len(img) == 0 and web.status == 200):
            return True
        alinks = soup.find_all('a', href=True)
        if(alinks):
            try:
                for alink in alinks:
                    if(alink.img):
                        thread = threading.Thread(target=self.extract_currurl_detail, args=(alink['href'],))
                        thread.start()
                        thread.join()
            except:
                logging.warning('Excepción en los hilos')
        return False
    
    def getFlag(self, img):
        url = self.url.format(img['src'])
        web = self.http.request('GET',url)
        return b64encode(web.data)


    def extract_currurl_detail(self,endpoint):
        url = self.url.format(endpoint)
        web = self.http.request('GET',url)
        soup = BeautifulSoup(web.data, 'lxml')
        trs = soup.find_all('tr')
        datos = {}
        for tr in trs:
            label = None
            for td in tr.find_all('td'):
                if td.get('class')[0] == 'w2p_fl':
                    try:
                        label = td.label.contents[0].strip().replace(":","")
                        datos[label] = None
                    except:
                        logging.warning('Excepcion con label')
                if td.get('class')[0] == 'w2p_fw':
                        if(len(td.contents) > 0 ):
                            try:
                                list_a = []
                                if(not isinstance(td.contents[0],NavigableString)):
                                    list_a = td.contents[0].find_all('a')    
                                if len(list_a) > 0:
                                    list_ap = []
                                    for elem_a in list_a:
                                        list_ap.append(elem_a.contents[0].strip())
                                    datos[label] = list_ap
                                else:
                                    if label == 'Continent':
                                        datos[label] = td.contents[0].contents[0]
                                    elif label == 'Flag':
                                        datos[label] = self.getFlag(td.contents[0]).decode('UTF-8')
                                    else:
                                        datos[label] = td.contents[0]
                            except:
                                logging.warning('Excepcion')
                                datos[label] = None
        self.lista.append(datos)

