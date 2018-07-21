> **介绍**

使用 scrapy 爬取代理网站，将获取到的大量代理ip保存到数据库。

> **环境**

如果需要爬取国外网站，本地必须可以翻墙，安装ss

> **抓取代理网站**

添加代理网站库，进行维护
* 【国外】https://www.us-proxy.org/
* 【国内】https://www.kuaidaili.com/free/
* 【国内】http://www.xicidaili.com/
* 【国内】http://www.data5u.com/free/index.shtml
* 【国内】http://m.66ip.cn/
* 【国内】http://www.goubanjia.com/

1. 有一个爬虫基类，导入配置的代理ip网址
2. 在处理请求的函数中，遍历所有的代理ip网址
3. 每一个网站的parse函数单独定义，统一在parse中处理，导入网址相对应的parse解析函数
4. 保存到数据库
5. 开启下载中间件，处理国外线路，走本地ss 1080端口代理

> **扩展**

1. 维护`const.py`里面的`SOURCE_URL`
2. 在`parse_methods.py`里面添加对应网站的解析函数，必须继承自基类`ParseMethodBase`
3. `SOURCE_URL`里面的name必须跟`ParseMethodBase`子类的类名一致
4. 解析函数将会在`base_spider.py`中统一处理调用，只要写好对应的解析函数即可
