"""
策略服务器开放时间
早 9：00 - 晚23：00
"""

import requests
import pandas as pd
import urllib
import time
import re
strategy_server = 'http://pq.simpledata.cn:8200'
start = '2020-06-15'
end = '2020-06-15'
# 代表前一天涨幅大于9.94%， 并且当天的换手率大于15%的股票, 更多因子和策略参考 www.simpledata.cn
strategy = 's_first_pctchange_2>=9.94 and s_first_turnover_1>15'
r = requests.get(strategy_server + '/query_engine?query={}&start={}&end={}'.format(urllib.parse.quote(strategy, 'utf-8'),
                                                                                             start,
                                                                                              end))
j = eval(r.text)
frame = pd.DataFrame(j['data'], index=pd.MultiIndex.from_tuples(j['index']), columns=j['columns'])
print(frame)