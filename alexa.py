# Mr wang
import json

import requests
import re

def get_alexa(domain):
    url=f'https://alexa.aizhan.com/{domain}/'
    headers={'Host': 'alexa.aizhan.com',
             'Referer': 'https://rank.aizhan.com/',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    r=requests.get(url=url,headers=headers,timeout=5)
    world_rank=re.findall('<li>全球排名：<span class="red">(.*?)</span>',r.text)[0]
    country_rank=re.findall('<li>全国排名：<span class="red">(.*?)</span>',r.text)[0]
    daily_ip=re.findall('<li>预估日均IP<span>≈(.*?)</span></li>',r.text)[0]
    daily_pv=re.findall('<li>预估日均PV<span>≈(.*?)</span></li>',r.text)[0]
    data={'world_rank':world_rank,'country_rank':country_rank,'daily_ip':daily_ip,'daily_pv':daily_pv}
    print(data)
    return  data
def get_baidurank(domain):
    key='623900f61b21ef2a54f0c92ce31dd4f5'
    url=f'https://apistore.aizhan.com/baidurank/siteinfos/{key}?domains={domain}'
    r=requests.get(url)
    results=json.loads(r.text)

    if results['code']==200000:
        for i in results['data']['success']:
            data={'pc_br': i['pc_br'], 'm_br': i['m_br'], 'ip': i['ip'], 'pc_ip': i['pc_ip'], 'm_ip': i['m_ip']}
            print(data)
    else:
        data=[]
    return data
if __name__ == '__main__':
    domain = input(u'请输入你要查找的域名')
    get_alexa(domain)
    get_baidurank(domain)
