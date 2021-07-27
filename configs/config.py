# -*- coding:utf-8 -*-

from fake_useragent import UserAgent
import random
import pandas as pd
import os


CITYNAME = '北京'
cities_path = os.path.dirname(os.path.realpath(__file__)) + '/utils/cities.json'
with open(cities_path, encoding='utf-8') as f:
    CITIES = eval(f.read())

BASE_URL = "https://{}.meituan.com/meishi/api/poi/getPoiList?".format(CITIES[CITYNAME])

# USER-AGENT
log_path = os.path.dirname(os.path.realpath(__file__)) + '/utils/ua.log'
df = pd.read_csv(log_path, sep='\t')
user_agent = df["UA"].iloc[random.randint(0,1000)]

HEADERS = {
    "Accept": "application/json",
    "Referer": "https://{}.meituan.com/".format(CITIES[CITYNAME]),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    # "User-Agent": UserAgent().random,
    # "User-Agent": user_agent
}

# UUID
uuid_path = os.path.dirname(os.path.realpath(__file__)) + '/utils/uuid.log'
with open(uuid_path) as f:
    UUID = f.read()

DATA = {
    "cityName": CITYNAME,
    "cateId": '0',
    "areaId": "0",
    "sort": "", # 控制排序方式[空表示默认排序，rating=好评最多，price_asc=价格升序，sales=销量]
    "dinnerCountAttrId": "",
    "page": "1",
    "userId": "96648282",
    # "uuid": UUID,
    "uuid": "ac1dfd7828e34c4c9578.1626856587.1.0.0",
    "platform": "1",
    "partner": "126",
    "originUrl": "https://{}.meituan.com/meishi/".format(CITIES[CITYNAME]),
    "riskLevel": "1",
    "optimusCode": "1"
}

# cookie信息，登录美团PC版从浏览器获取
COOKIE = {
'_lxsdk_cuid=17a9a3a3bf6c8-0711e462dd173-34647600-384000-17a9a3a3bf6c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; userTicket=bBfkrzIdOzmNBSCCJVpHrEgzDAdfWpqiLbEYnfYo; lsu=; _lxsdk=17a9a3a3bf6c8-0711e462dd173-34647600-384000-17a9a3a3bf6c8; _hc.v=675b10b1-1eb3-92e8-15ba-676cbe3e17a4.1626093831; lat=39.893071; lng=116.465853; uuid=4411144c0b504ba4ae3b.1626146478.1.0.0; ci=10; rvct=10%2C1; client-id=57594ef8-a230-48e9-8166-b9cb67d9dbc9; lt=WO6At48AbecSeiX29vAiGMt5skAAAAAACw4AAImEgd2gpW0LTe8FNfKn2tYkKXYv0v-D-VPmG0v6BsCborVMVSABKa8vNHLi6BfISQ; u=96648282; n=%E8%BF%9F%E6%81%A96; token2=WO6At48AbecSeiX29vAiGMt5skAAAAAACw4AAImEgd2gpW0LTe8FNfKn2tYkKXYv0v-D-VPmG0v6BsCborVMVSABKa8vNHLi6BfISQ; unc=%E8%BF%9F%E6%81%A96; __mta=217888297.1626231335083.1626265934142.1626265980210.6; firstTime=1626265991077; _lxsdk_s=17aa500b682-341-345-e2c%7C%7C9'
}

# GET PARAMETER
GET_PARAM =  {
        "cityName": DATA["cityName"],
        "cateId": DATA["cateId"],
        "areaId": DATA["areaId"],
        "sort": DATA["sort"],
        "dinnerCountAttrId": DATA["dinnerCountAttrId"],
        "page": DATA["page"],
        "userId": DATA["userId"],
        "uuid": DATA["uuid"],
        "platform": DATA["platform"],
        "partner": DATA["partner"],
        "originUrl": DATA["originUrl"],
        "riskLevel": DATA["riskLevel"],
        "optimusCode": DATA["optimusCode"],
        # "_token": encrypt_token()
}

# SIGN PARAMETER
SIGN_PARAM = "areaId={}&cateId={}&cityName={}&dinnerCountAttrId={}&optimusCode={}&originUrl={}&page={}&partner={}&platform={}&riskLevel={}&sort={}&userId={}&uuid={}".format(
    DATA["areaId"],
    DATA["cateId"],
    DATA["cityName"],
    DATA["dinnerCountAttrId"],
    DATA["optimusCode"],
    DATA["originUrl"],
    DATA["page"],
    DATA["partner"],
    DATA["platform"],
    DATA["riskLevel"],
    DATA["sort"],
    DATA["userId"],
    DATA["uuid"]
)

# TIME OUT
TIMEOUT = 5

# MAX PAGES
MAX_PAGES = 67

# MYSQL SETTINGS
HOST = 'localhost'
USER = 'root'
PASS = 'Root1234'
PORT = 3306
DB = 'meituan'
TABLE = 'meishi'

# PROXY API
API = ''

# PROXY SETTINGS
PROXY_HOST = "http-dyn.abuyun.com"
PROXY_PORT = "9020"
PROXY_USER = "HU4C31nmfiDR57D"
PROXY_PASS = "2D4F3B8489F5FC91"

if __name__ == '__main__':
    # print(os.path.dirname(os.path.realpath(__file__)))
    pass
