# -*- coding: utf-8 -*-
# first initialization : source hamu/bin/active
from lib.util.get_code import *
from lib.get_price import *
from lib.get_real_price import *
from lib.util.logger import *

# initialized logger
init_logger()

area_code = '4113510700' # 야탑동 (법정동 코드 https://goo.gl/P6ni8Q 참조)
apt_name = '매화마을공무원2단지' # 장미8단지현대, 탑벽산
min_date = '19.10.01'

get_naver_realasset(area_code, apt_name, min_date)

# df = pd.DataFrame()
# for i in range(1, 50): # 최대 100 페이지
#     df_tmp = get_naver_realasset(area_code, apt_name, min_date,i)
#     if len(df_tmp) <= 0:
#         break
#     df = df.append(df_tmp, ignore_index=True)

# print df

# 6334 장미마을, 6315 매화마을 2단지, 6339 벽산, 6360 청라한솔
# get_detail_real_price(6315, 2019)
# get_detail_real_price(50369, 2019)

# get_avg_real_price(6334, 2019)

# p = '경기도 성남시 분당구 야탑동'
# df_province = get_province(p)
# value = df_province.loc[df_province['법정동명'] == p, '법정동코드'].values[0]
