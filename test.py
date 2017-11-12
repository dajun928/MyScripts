# coding:utf-8
import requests

headers = {
	'Host': 'unsplash.com',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Connection': 'keep-alive',
}

url = 'https://unsplash.com/'
ret = requests.get(url)
print ret.status_code
print ret.text

