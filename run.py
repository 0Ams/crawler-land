# -*- coding: utf-8 -*-
# first initialization : source hamu/bin/active
from lib.util.get_code import *
from lib.get_price import *
from lib.get_real_price import *
from lib.util.logger import *
import time
now = time.localtime()
YEAR = now.tm_year

# initialized logger

area_code = '4113510700' # 야탑동 (법정동 코드 https://goo.gl/P6ni8Q 참조)
apt_name = '매화마을공무원2단지' # 장미8단지현대, 탑벽산
min_date = '19.10.01'
AREA_CODE_TABLE = {
    6334: '장미마을 현대',
    6315: '매화마을 2단지',
    6339: '야탑 벽산',
    6360: '청라한솔',
    50369: '정자 정든마을'
}

def initialization():
  init_logger()
  return logging.getLogger("logger")

def run():
  logger = initialization()
  arg = input(f"1. 네이버 호가 검색 => naver \n2. 실거래가 => real \n3. 실거래가 모두 => real-all\n입력해주세요: ")
  if arg == 'naver':
    get_naver_realasset(area_code, apt_name, min_date)
  elif arg == 'real':
    f = open(f"{YEAR}-realprice.md", "a")
    target = int(input(f"6334: '장미마을' \n6315: '매화 2단지' \n6339: '벽산' \n6360: '청라한솔' \n50369: '정자 정든마을' \n: "))
    result = get_detail_real_price(target, YEAR)
    print(result, file=f)
    f.close()
  elif arg == 'real-all':
    f = open(f"{YEAR}-real-price-all.md", "w")
    result = "# 실거래가 모음\n"
    for key in AREA_CODE_TABLE.keys():
      result += get_detail_real_price(key, YEAR)
    print(result, file=f)
    f.close()
  else:
    logger("input 값이 이상함")

run()
# df = pd.DataFrame()
# for i in range(1, 50): # 최대 100 페이지
#     df_tmp = get_naver_realasset(area_code, apt_name, min_date,i)
#     if len(df_tmp) <= 0:
#         break
#     df = df.append(df_tmp, ignore_index=True)

# 6334 장미마을, 6315 매화마을 2단지, 6339 벽산, 6360 청라한솔, 50369 정자 정든마을
# get_detail_real_price(6315, 2019)
# get_detail_real_price(50369, 2019)
# get_avg_real_price(6334, 2019)

# p = '경기도 성남시 분당구 야탑동'
# df_province = get_province(p)
# value = df_province.loc[df_province['법정동명'] == p, '법정동코드'].values[0]
