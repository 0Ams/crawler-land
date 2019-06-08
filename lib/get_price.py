#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import re


def get_naver_realasset(area_code, apt_name, min_date, page=1):
  url = 'http://land.naver.com/article/articleList.nhn?' \
      + 'rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04' \
      + '&minPrc=30000' \
      + '&maxPrc=60000' \
      + '&cortarNo=' + area_code \
      + '&page=' + str(page)

  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'lxml')

  table = soup.find('table')
  trs = table.tbody.find_all('tr')
  
  if '등록된 매물이 없습니다' in trs[0].text:
    return pd.DataFrame()

  value_list = []

  # 거래, 종류, 확인일자, 매물명, 면적(㎡), 층, 매물가(만원), 연락처
  # _deal, _type, _checkDate, _name, _areaSize, _publicSize, _privateSize, _price, _contract
  for tr in trs[::2]:
    tds = tr.find_all('td')
    cols = [' '.join(td.text.strip().split()) for td in tds]


    if apt_name not in cols[3]:
      continue
    if datetime.strptime(cols[2], '%y.%m.%d.') < datetime.strptime(min_date, '%y.%m.%d'):
      continue

    if '_thumb_image' not in tds[3]['class']:  # 현장확인 날짜와 이미지가 없는 행
        cols.insert(3, '')

    _deal = cols[0]
    _type = cols[1]
    _checkDate = datetime.strptime(cols[2], '%y.%m.%d.')
    _confirmCheck = cols[3]
    _name = cols[4]
    _areaSize = cols[5]

    _publicSize = re.findall(unicode('공급면적(.*?)㎡'), _areaSize)[0].replace(',', '')
    _privateSize = re.findall(unicode('전용면적(.*?)㎡'), _areaSize)[0].replace(',', '')
    _publicSize = float(_publicSize)
    _privateSize = float(_privateSize)
    # _publicSize = re.findall(r'\d*\/', _areaSize)[0].replace('/', '')
    # _privateSize = re.findall(r'\/\d*', _areaSize)[0].replace('/', '')

    _stair = cols[6]
    if cols[7].find('호가일뿐 실거래가로확인된 금액이 아닙니다') >= 0:
      pass  # 단순호가 별도 처리하고자 하면 내용 추가
    _price = int(cols[7].split(' ')[0].replace(',', ''))
    _contract = cols[8]
    value_list.append([_deal, _type, _checkDate, _confirmCheck,
                        _name, _publicSize, _privateSize, _stair, _price, _contract])

  cols = ['거래', '종류', '확인일자', '현장확인', '매물명',
          '공급면적', '전용면적', '층', '매물가', '연락처']
  df = pd.DataFrame(value_list, columns=cols)
  return df
