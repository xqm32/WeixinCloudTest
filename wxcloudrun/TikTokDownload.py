import requests
import re
import json


def getVideoUrl(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }

    shortRes = requests.get(url)
    key = re.findall('video/(\d+)?', str(shortRes.url))[0]
    # 官方接口
    iesRes = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'
    realLink = json.loads(requests.get(url=iesRes, headers=headers).text)
    return realLink['item_list'][0]['video']['play_addr']['url_list'][0].replace(
        'playwm', 'play')


def getRealUrl(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }

    shortRes = requests.get(url)
    key = re.findall('video/(\d+)?', str(shortRes.url))[0]
    # 官方接口
    iesRes = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'
    realLink = json.loads(requests.get(url=iesRes, headers=headers).text)
    jumpLink = realLink['item_list'][0]['video']['play_addr']['url_list'][0].replace(
        'playwm', 'play')

    return requests.get(jumpLink, headers=headers, allow_redirects=False).headers['Location']
