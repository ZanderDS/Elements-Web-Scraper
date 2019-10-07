# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:08:16 2019

@author: zander
"""
import pandas as pd
import re
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

element_table = soup.find('table', attrs={'class': 'wikitable'})

element_table_data = element_table.tbody.find_all('tr')

letter_pattern = r'\[[A-Z]*?\]'
everything_pattern = r'\[.*?\]'

title = []
headings = []
symbol = []
table_row = []
table = {}

for x in element_table_data[0].find_all('th'):
  title.append(x.get_text().strip())

for x in element_table_data[1].find_all('th'):
  headings.append(re.sub(everything_pattern, '', x.get_text().strip()))

for i in range(4,122):
  symbol.append(element_table_data[i].find_all('td')[1].get_text())
  
for x, i in zip(symbol, range(4,122)):
  table_row = []
  for z in range(0,13):
    table_row.append(re.sub(letter_pattern, '', element_table_data[i].find_all('td')[z].get_text()))
    
  table[x] = dict(zip(headings, table_row))

df = pd.DataFrame(table)
df.to_json('elements.json')
print(df)
print('Successfully saved to .json format')
  
  





 
  
#hier_index = list(zip(headings))

#df = pd.DataFrame(random.randn(118,1),hier_index)
# =============================================================================
# for i in range(4:122):
#   row_data = []
#   for x in element_table_data[i].find_all('td'):
#     row_data.append(x.get_text().strip())
# =============================================================================



  
#print(headings)
# =============================================================================
# source = urlopen(url).read()
# 
# soup = BeautifulSoup(source, 'html.parser')
# 
# tables = soup.find_all('table')
# 
# table_rows = tables[0].find_all('tr')
# 
# for tr in table_rows:
#   print(tr)
# =============================================================================
