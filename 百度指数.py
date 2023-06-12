# -*- coding: UTF-8 -*-
'''
	较之domain_flu，域名 和 标题 精确查询的数值都太少， 尤其是域名， 因此去除二者的精确查询
'''

import requests
import re
import time

import sys
import importlib


headers = {"Accept": "text/html;",
	            "Accept-Language": "zh-CN,zh;q=0.8",
	            "Referer": "http://www.baidu.com/",
	            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
	            }





# 在这里对获取到的counts数组进行处理，如果只有域名查询数量的数据，则直接返回该数据即可;
# 若还有title查询的数据， 则对数据进行如下处理：0.8 * counts[0] + 0.2 * counts[1]， 即分别赋予其0.8 和 0.2 的权重进行计算
def data_handle(counts):
    if len(counts) == 1:
        return counts[0]
    else:
        index = 0.8 * counts[0] + 0.2 * counts[1]
        return index


def Baidu_get_raw_html(domain, title):
    wd_list = []
    wd_list.append(domain)
    if title != '':
        wd_list.append(title)
    counts = []
    for item in wd_list:
        ini_payload = {'wd': item, 'pn': str(0)}
        try:
            ini_html = requests.get('https://www.baidu.com/s', params=ini_payload, headers=headers, timeout=5).text
            if '很抱歉，没有找到' in ini_html:
                counts.append(0)
                continue
            total_pages = re.compile(r'<div class="search_tool" ><i class="c-icon searchTool-spanner c-icon-setting"></i>.+?(</div>.+?</div>)</div></div>').findall(ini_html)[0].replace(',', '')
            total_pages = int(re.compile(r'</div>.*?(\d+).*</div>').findall(total_pages)[0])
            counts.append(total_pages)
        except:
            print(domain, item)
            return 0
    index = data_handle(counts)
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(index, date)
    return index




if __name__ == '__main__':

    title = '香港赛马会|www.08111.com|香港挂牌|香港六合彩|香港马会开奖结果|开奖结果|香港六合彩特码图库|曾道人|白小姐|惠泽社群|香港赛马会|六合彩开奖记录|'
    domain = '388488.com'
    Baidu_get_raw_html(domain, title)