
# 代理ip网站域名,(url, name, 是否是国内) 
SOURCE_URL = [
    ('https://www.us-proxy.org/', 'us-proxy', False),
    ('https://www.kuaidaili.com/ops/proxylist/1/', 'kuaidaili', True),
    ('http://www.xicidaili.com/', 'xicidaili', True),
    ('http://www.data5u.com/free/index.shtml', 'data5u', True),
    ('http://m.66ip.cn/', '66ip', True),
    ('http://www.goubanjia.com/', 'goubanjia', True)
]

# 本地mongo数据库信息
MONGO_HOST = '192.168.0.101'
MONGO_PORT = 27017
MONGO_DB = 'ip_proxy'
MONGO_COLLECTION = 'proxies'
MONGO_CONNSTR = 'mongodb://ip_proxy:123@192.168.0.101:27017/ip_proxy'