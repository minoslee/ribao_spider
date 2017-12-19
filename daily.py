import requests
import re
from bs4 import BeautifulSoup
import os
import os.path
import pdfkit
import time
from time import strftime

class ribao(object):
	def __init__(self):
		self.home_url = 'http://daily.zhihu.com'
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
		self.content_url = []
		self.local_path = r'G:\python\zhihu\ribao\book'
		self.all_title = []

	def home_html(self):
		content = requests.get(self.home_url,headers = self.headers)
		all_href = BeautifulSoup(content.text,'lxml').find_all('a',class_ = 'link-button')
		all_title = BeautifulSoup(content.text,'lxml').find_all('span',class_ = 'title')

		for href in all_href:
			url = self.home_url + href['href']
			self.content_url.append(url)

		for title in all_title:
			title = title.get_text()
			title = title.replace(" ",'_')
			self.all_title.append(title.replace('/','_'))

		self.content_html()

	def change_dir(self):
		t = time.strftime("%Y%m%d") #获取当前日期
		folder = self.local_path + '\\'+ str(t)
		print(folder)
		if os.path.exists(folder):
			os.chdir(folder)
		else:
			os.mkdir(folder)
		os.chdir(folder)

	def content_html(self):
		self.change_dir()
		cnt = 0;
		options = {
		    'page-size': 'Letter',
		    'margin-top': '0.75in',
		    'margin-right': '0.75in',
		    'margin-bottom': '0.75in',
		    'margin-left': '0.75in',
		    'encoding': "UTF-8",
		    'disable-javascript':None, # 不禁用pdfkit会蜜汁报错
		    }
		
		for url in self.content_url:
			title = self.all_title[cnt]
			path = title.strip()[0:20]
			file_name = str(path) + '.pdf'
			# print(file_name)
			if os.path.exists(str(file_name)):
				pass	
			else:
				print('正在保存：%s'%title)
				pdfkit.from_url(url,str(file_name) ,options = options)
			cnt += 1
		print('保存完毕，共%d个文件'%cnt)

if __name__ == '__main__':
	Ribao = ribao()
	Ribao.home_html()

