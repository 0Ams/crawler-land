# -*- coding: utf-8 -*-
from lib.util.get_code import *
from lib.get_price import *

area_code = '4113510700' # 야탑동 (법정동 코드 https://goo.gl/P6ni8Q 참조)
apt_name = '매화마을공무원2단지'
min_date = '19.06.03'

df = pd.DataFrame()
for i in range(1, 50): # 최대 100 페이지
    df_tmp = get_naver_realasset(area_code, apt_name, min_date,i)
    if len(df_tmp) <= 0:
        break
    df = df.append(df_tmp, ignore_index=True)

print df

# p = '경기도 성남시 분당구 야탑동'
# df_province = get_province(p)
# value = df_province.loc[df_province['법정동명'] == p, '법정동코드'].values[0]
