# -*- coding: utf-8 -*-
import requests
import json
import logging

URL = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do"
HEADER = {
    'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND'
}

AREA_CODE_TABLE = {
    6334: '장미마을 현대',
    6315: '매화마을 2단지',
    6339: '야탑 벽산',
    6360: '청라한솔',
    50369: '정자 정든마을'
}
logger = logging.getLogger("logger")

# 6334 장미마을, 6315 매화마을 2단지, 6339 벽산, 6360 청라한솔


def get_detail_real_price(code, year):
  param = {
      'menuGubun': 'A',
      'p_apt_code': code,
      'p_house_cd': 1,
      'p_acc_year': year
  }

  resp = requests.get(URL, params=param, headers=HEADER)
  if resp.status_code != 200:
      logger.error('invalid status: %d' % resp.status)
      exit

  data = json.loads(resp.text)
  result = "<details>"+f"<summary>[{AREA_CODE_TABLE[code]} 실거래가] </summary>"+"<div markdown='1'>\n"+"\n|계약 날짜|층|크기|가격|\n"+"|--|--|--|--|\n"
  for item in data['result']:
      if item['BLDG_AREA'] < 55 or item['BLDG_AREA'] > 90:
          continue
    #   result += f"[{AREA_CODE_TABLE[code]}][{item['DEAL_MM']}월] {item['APTFNO']}층 크기: {item['BLDG_AREA']}㎡ 가격 {item['SUM_AMT']}만원\n"
      result += f"|{item['DEAL_MM']}월|{item['APTFNO']}층|{item['BLDG_AREA']}㎡|{item['SUM_AMT']}만원|\n"

  result+="\n</div>"+"</details>"
  logger.info(result)
  return result


# Size에 따라 가격이 변하므로 큰 의미는 없는 데이터가됨.
def get_avg_real_price(code, year):
  param = {
      'menuGubun': 'A',
      'p_apt_code': code,
      'p_house_cd': 1,
      'p_acc_year': year
  }

  resp = requests.get(URL, params=param, headers=HEADER)
  if resp.status_code != 200:
      logger.error('invalid status: %d' % resp.status)
      exit

  data = json.loads(resp.text)
  realPrice = {}

  for item in data['result']:
      if item['BLDG_AREA'] < 55 or item['BLDG_AREA'] > 90:
        continue
      if realPrice.get(item['APTFNO']) is None:
        realPrice[item['APTFNO']] = {'total': 0, 'count': 1}
      realPrice[item['APTFNO']]['total'] = int(
          realPrice[item['APTFNO']]['total']) + int(item['SUM_AMT'].replace(",", ""))
      realPrice[item['APTFNO']]['count'] = realPrice[item['APTFNO']]['count'] + 1

  result = '\n======================== 평균 실거래가 =============================\n'
  for floor in realPrice.keys():
      result += f"[{floor}층] 평균가격: {realPrice[floor]['total']/realPrice[floor]['count']}\n"

  return result
