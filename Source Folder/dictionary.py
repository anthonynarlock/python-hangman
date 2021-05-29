#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import re
from requests import get

class dictionary:
  def remove_non_ascii(self,text):
    return re.sub(r'[^\x00-\x7F]+','', text)

  def get_soup(self,url):
    raw = self.remove_non_ascii(get(url).content)
    soup = bs(raw)
    return soup.select("#MainTxt")[0].select('.ds-single')[0].text.strip()

  def lookup(self,word):
    base_url  = "http://www.thefreedictionary.com/"
    query_url = base_url + word
    return self.get_soup(query_url)