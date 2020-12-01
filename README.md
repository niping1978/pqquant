# pqquant
数据获取方式:
-----------
订阅号，微信搜索  “向财而生”, 关注->进入订阅号->点击 "帮助"  获取百度网盘地址。<br>
网站地址: www.simpledata.cn<br>
免费提供a股各种逐笔数据，板块信息，最最重要的是我们提供了全网唯一的真正能实战的策略服务器，帮助quant客专注于业务和策略，而非技术。<br>

逐笔数据源格式:
-------------
TranID,Time,Price,Volume,SaleOrderVolume,BuyOrderVolume,Type,SaleOrderID,SaleOrderPrice,BuyOrderID,BuyOrderPrice<br>
1,09:25:00,44.36,100,100,1100,S,1,39.60,1,48.40<br>
2,09:25:00,44.36,100,100,1100,S,2,39.60,1,48.40<br>

分钟线数据提供 `通达信格式，每6天更新一次`。
带有`逐笔ID`的数据，每三天更新一次。
数据获取地址每7天更新一次，订阅号内获取。

此项目解决了三个问题:
------------------
1. 量化客寻找不到免费的高质量数据源，比如逐笔level2数据， 1分钟线数据等。<br>
2. 对于写量化策略，往往非常难以找到非常快的方式实现所想。争取1分钟实现一个策略，更多的精力放在赚钱层面。<br>
3. 对于复盘，我们提供了 pq投顾.exe, 应该是目前最好用的复盘工具和股票选择器软件, 下载地址:www.simpledata.cn。<br>


>>我们提供数据、策略服务、软件平台，其中自己写策略，发送给策略服务器，返回满足条件的股票。<br>
>>因子手册参见 www.simpledata.cn<br>

因子说明
--------
系统中不仅进行了因子开发，并且对因子进行了操作，


简单示例策略
-----------
strategy = 's_first_pctchange_2>=9.94 and s_first_turnover_1>15'
代表前一天涨幅大于9.94%， 并且当天的换手率大于15%的股票，

策略执行，参考 strategy.py 文件。

经典策略解析
-----------
>>庄家吃货
(s_first_bs_1+s_first_ms_1)/(s_first_bb_1+s_first_mb_1) > 1.5 and s_first_pctchange_1>0 and s_first_pctchange_1<5 and s_first_turnover_1>5 and s_first_turnover_1<20  and (s_first_bs_1/s_ma_bs_5)>1.5
本策略描述了在庄家主动卖较多，但是价格没有下降的，换手率也较高，并且(s_first_bs_1/s_ma_bs_5)>1.5 大单卖的量比平均5天来的平均量大于1.5倍，


欢迎关注 向财而生(量化实战) 订阅号<br>
-------------------------------
![QRCODE](https://github.com/niping1978/pqquant/blob/main/qrcode.jpg)

备注:
目前策略服务器开放时间:
早 9:00 ~ 晚 23：00

