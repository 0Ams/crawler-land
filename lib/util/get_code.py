# -*- coding: utf-8 -*-
import pandas as pd

def get_areacode():
  df_areacode = pd.read_csv('https://goo.gl/tM6r3v',
                            sep='\t', dtype={'법정동코드': str, '법정동명': str})
  df_areacode = df_areacode[df_areacode['폐지여부'] == '존재']
  df_areacode = df_areacode[['법정동코드', '법정동명']]
  return df_areacode

def get_province(name):
  df_areacode = get_areacode()
  df_province = df_areacode[df_areacode['법정동명'].str.contains(name)]
  return df_province
