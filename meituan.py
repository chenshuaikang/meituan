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
    COOKIE = '_lxsdk_cuid=17a9a3a3bf6c8-0711e462dd173-34647600-384000-17a9a3a3bf6c8; lsu=; _hc.v=675b10b1-1eb3-92e8-15ba-676cbe3e17a4.1626093831; uuid=8f219f2b8b3c41e3b7bd.1626695556.1.0.0; userTicket=wLWdxwrGuYwkBtOMcEYIkFntugDpfePwQiwbEnyo; ci=1; rvct=1%2C10; client-id=0229a7a0-4750-471c-ba83-7e526d26622f; _lxsdk=17a9a3a3bf6c8-0711e462dd173-34647600-384000-17a9a3a3bf6c8; mtcdn=K; lt=DqAMEhgPXKVGmI6efmzY2YWnWgYAAAAACw4AAKxbFAOlul_fDzLP67HROQeXiRr5xaV324Kd8LzwMdgzxVj75ir-1LP8QhKcnXfjGw; u=96648282; n=%E8%BF%9F%E6%81%A96; token2=DqAMEhgPXKVGmI6efmzY2YWnWgYAAAAACw4AAKxbFAOlul_fDzLP67HROQeXiRr5xaV324Kd8LzwMdgzxVj75ir-1LP8QhKcnXfjGw; __mta=20706055.1626093469721.1626783390833.1626783468191.11; unc=%E8%BF%9F%E6%81%A96; firstTime=1626783474452; _lxsdk_s=17ac3d89b77-8a-be9-ab2%7C%7C6'
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
        time.sleep(random.randint(1,3))

    # 可视化分析
    view = View()
    view.meishi_top10()
    # view.avgprice_comments()
    # view.avgscore_ratio()
    # view.wrodcloud()
