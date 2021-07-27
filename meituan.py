#  -*- coding:utf-8 -*-

from configs.token_ import encrypt_token
from urllib.parse import urlencode
from common import save
from configs.parse import parse_json
import logging
import json
import requests
import time
import random
from configs.config import GET_PARAM, HEADERS, TIMEOUT, MAX_PAGES, BASE_URL
from configs.visual import View

def main(base_url, page):
    """主函数"""
    # 添加_token参数
    GET_PARAM["_token"] = encrypt_token()
    GET_PARAM['page'] = str(page)
    url = base_url + urlencode(GET_PARAM)
    # proxies = xdaili_proxy()
    # session = requests.Session()
    # response = json.loads(session.get(url, headers=HEADERS, proxies=proxies, timeout=TIMEOUT).text)
    # print(url)
    # 替换成自己的已登录的cookie
    COOKIE = '_lxsdk_cuid=17ac8358148c8-05e6e923a97b4c-34637600-13c680-17ac8358148c8; ci=1; rvct=1; mtcdn=K; userTicket=esAWEmvJnDRnPtIvmKjpOakOmtbTPTAuLahpcSkd; lsu=; _lxsdk=17ac8358148c8-05e6e923a97b4c-34637600-13c680-17ac8358148c8; u=96648282; n=%E8%BF%9F%E6%81%A96; lt=OIyYI-lEP1W0h_3QsFpTWHfRVpAAAAAAMQ4AACHgkz9Ud1s7Bji2ss_JfrFI0_JqxJrEKcI_IzROEQ0DAR9Kokhn1VfrjPDElEYYOg; mt_c_token=OIyYI-lEP1W0h_3QsFpTWHfRVpAAAAAAMQ4AACHgkz9Ud1s7Bji2ss_JfrFI0_JqxJrEKcI_IzROEQ0DAR9Kokhn1VfrjPDElEYYOg; token=OIyYI-lEP1W0h_3QsFpTWHfRVpAAAAAAMQ4AACHgkz9Ud1s7Bji2ss_JfrFI0_JqxJrEKcI_IzROEQ0DAR9Kokhn1VfrjPDElEYYOg; token2=OIyYI-lEP1W0h_3QsFpTWHfRVpAAAAAAMQ4AACHgkz9Ud1s7Bji2ss_JfrFI0_JqxJrEKcI_IzROEQ0DAR9Kokhn1VfrjPDElEYYOg; unc=%E8%BF%9F%E6%81%A96; __mta=119970231.1626856590396.1626964435545.1627389984295.13; client-id=2aedb251-7b3f-4b15-afbc-a6e11362e2e8; firstTime=1627389989395; _lxsdk_s=17ae8004117-1bf-9e7-f6b%7C%7C6'
    cookies = {i.split('=')[0]: i.split('=')[1] for i in COOKIE.split('; ')}
    response = json.loads(requests.get(url, headers=HEADERS, cookies=cookies, timeout=TIMEOUT).text)
    # print(response)
    try:
        infos = response['data']['poiInfos']
        i = 0
        for info in infos:
            data = parse_json(info)
            print(data, sep='\n')
            save(data)
    except Exception as e:
        logging.warning(" Response status code: {}, Requests was found, no target data was obtained!".format(response['code']))
        _ = e

if __name__ == '__main__':
    # 多进程
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # for page in range(1, MAX_PAGES + 1):
    #     pool.apply_async(main, (BASE_URL, page))
    # pool.close()
    # pool.join()

    # 获取数据
    for page in range(1, MAX_PAGES + 1):
        main(BASE_URL, page)
        time.sleep(random.randint(10,20))

    # 可视化分析
    view = View()
    view.meishi_top10()
    # view.avgprice_comments()
    # view.avgscore_ratio()
    # view.wrodcloud()
