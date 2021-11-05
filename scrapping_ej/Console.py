#!/usr/bin/env python
import argparse
from .Scrapper import Scrapper
from .BaseController import BaseController
from os import path
import json

import logging
logging.basicConfig(filename='./scrapping-ej.log', level=logging.DEBUG)

class Console(object):
  def __init__(self):
      self.parser = argparse.ArgumentParser()
      self.args = None
  
  def argumentParse(self):
      self.parser.add_argument('--url',nargs='?',type=str, default="http://example.python-scraping.com{}",help='url base de donde iniciara la extracción')
      self.parser.add_argument('--proxy',nargs='?',type=str,help='Url de la proxy que se usara')
      self.args = self.parser.parse_args()
  
  def iniciar(self):
    logging.info('Inicio de extracción')
    self.argumentParse()
    sc = Scrapper(self.args.url, self.args.proxy)
    sc.extract_currurl()
    bc = BaseController()
    for elem in sc.lista:          
      bc.insertData(elem)
    bc.conn.close()
    json_lista = json.dumps(sc.lista)
    with open('res.json', 'w') as f:
      f.write(json_lista)
