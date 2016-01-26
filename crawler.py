# coding=UTF-8
import urllib
import urllib2
import requests
from pyquery import PyQuery as pq
from urllib import urlretrieve
import time
import shutil
import os
# from bs4 import BeautifulSoup

def webcrawler(url):
	# plantname = '廣東油桐'
	# problemarray = ["http://kplant.biodiv.tw/呂宋水錦樹/呂宋水錦樹.htm",
	# 				"http://kplant.biodiv.tw/紅苞花/紅苞花.htm",
	# 				"http://kplant.biodiv.tw/一串紅/一串紅.htm",
	# 				"http://kplant.biodiv.tw/臺灣蒲公英/臺灣蒲公英.htm"]

	# if url not in problemarray:
	data = []
	# othername = []
	# englishname = []
	try:
		res = requests.get(url)
	# res = requests.get("http://kplant.biodiv.tw/" + plantname + "/" + plantname + ".htm")
	#     res = requests.get("http://www.i-part.com.tw/diary/diary_my.php?o=4494259");
	# res.encoding = 'cp950'
		res.encoding = res.apparent_encoding                                       
	# print(res.text)
	# pagehtml = ''
	# for line in res.text:
	#     pagehtml += line
	    # print(line)
		page = pq(res.text)

		# print page
		count = 1
		# 中文名稱
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		isdo = False
		if (u"中文名稱" in page_content) == True:
			isdo = True
		elif(u"中 文 名 稱" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			page_content_name = page_content_split[1].split(u' ')
			# print page_content_name
			count = count + 1
			# data.append("\'"+page_content_name[1]+"\'")
			data.append(page_content_name[1])

		# 英文名稱
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		# print page_content_name
		isdo = True
		# print (page_content)
		# if (u"英文名稱" in page_content) == True:
		# 	isdo = True
		# elif(u"英 文 名 稱" in page_content) == True:
		# 	isdo = True
		# else:
		# 	data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			page_content_name = page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ' ').split(u'\uff0c')
			englishname = ""
			for index in page_content_name:
				# englishname.append("\'"+index+"\'")
				englishname = englishname + '\\' + index
				# englishname.append(index)
			# print englishname
			data.append(englishname)
			count = count + 1

		# 學名
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()

		isdo = True
		# if (u"學名" in page_content) == True:
		# 	isdo = True
		# elif(u"學 名" in page_content) == True:
		# 	isdo = True
		# else:
		# 	data.append(" ")
		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			page_content_name = page_content_split[1].replace('  ', '').replace('\r', '').replace('\n', ' ')
			# print page_content
			# data.append("\'"+page_content_name+"\'")
			# print page_content_name
			data.append(page_content_name)
			count = count + 1

		# 科別
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		
		isdo = True
		# if (u"科名" in page_content) == True:
		# 	isdo = True
		# elif(u"科別" in page_content) == True:
		# 	isdo = True
		# elif(u"科 別" in page_content) == True:
		# 	isdo = True
		# elif(u"科 名" in page_content) == True:
		# 	isdo = True
		# else:
		# 	data.append(" ")
		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			page_content_name = page_content_split[1].replace(' ', '')
			# print page_content_name
			# data.append("\'"+page_content_name+"\'")
			data.append(page_content_name)
			count = count + 1

		# 別名
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		
		isdo = True
		# if (u"別名" in page_content) == True:
		# 	isdo = True
		# elif(u"別 名" in page_content) == True:
		# 	isdo = True
		# else:
		# 	data.append(" ")
		
		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			page_content_name = page_content_split[1].replace(' ', '').replace(u'\uff0c', u'\u3001').replace(u'；', u'\u3001').split(u'\u3001')
			# print page_content_name
			othername = data[0]
			for index in page_content_name:
				# othername.append("\'"+index+"\'")
				# othername.append(index)
				othername = othername + "\\" + index
			# print othername
			data[0] = othername
			count = count + 1

		# 原產地
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
		isdo = False
		if (u"原產地" in page_content) == True:
			isdo = True
		elif(u"原 產 地" in page_content) == True:
			isdo = True
		else:
			# data.append("\' \'" )
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			count = count + 1

		# 分佈
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
		# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
		isdo = False
		if (u"分佈" in page_content) == True:
			isdo = True
		elif (u"分布" in page_content) == True:
			isdo = True
		elif(u"分 布" in page_content) == True:
			isdo = True
		elif(u"分 佈" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			count = count + 1

		# 用途
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		
		isdo = False
		if (u"用途" in page_content) == True:
			isdo = True
		elif(u"用 途" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			# print (u"用途" in page_content)
			page_content_split = page_content.split(u'\uff1a' + ' ')
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			application = ""
			for index in page_content_split:
				application = application + index.replace(' ', '').replace('\r', '').replace('\n', '')
				# print application
			# data.append("\'"+ application +"\'")
			data.append(application)
			# print application
			count = count + 1

		# 莖
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		
		isdo = False
		if (u"莖" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			count = count + 1

		# 葉
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()

		isdo = False
		if (u"葉" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			count = count + 1

		# 花
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		
		isdo = False
		if (u"花" in page_content) == True:
			isdo = True
		else:
			data.append(" ")

		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			count = count + 1

		# 果實
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()

		isdo = False
		if (u"果" in page_content) == True:
			isdo = True
		else:
			data.append(" ")	
		
		if isdo == True:
			page_content_split = page_content.split(u'\uff1a')
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
			data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
			# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
			count = count + 1

		# 特徵
		page_content = page('body > table:nth-child(2) > tr:nth-child(' + str(count) + ')').text()
		page_content_split = page_content.split(u'\uff1a')
		# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')
		# data.append("\'"+page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')+"\'")
		data.append(page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', ''))
		# print page_content_split[1].replace(' ', '').replace('\r', '').replace('\n', '')

		

		# print data
		return 0, data
	except:
		return 1, data

def imgsource(url):
	
	data = []
	picname = []
	plantname = ""
	req = 0

	try:
		res = requests.get(url)
		res.encoding = res.apparent_encoding
		page = pq(res.text)
		# print page
		# page_content = page('a > font').text()
		# try:
		page_content = page('body > table:nth-child(1) > tr:nth-child(1)').text()
		plantname = page_content
		page_content = page('body > table:nth-child(1) > tr:nth-child(3)').text().split(u' ')
		# print page_content
		# for x in page_content:
		# 	print x
		for x in page_content:
			data.append("http://kplant.biodiv.tw/" + plantname + "/" + x + ".jpg")
			picname.append(x)
	except:
		req = 1

	try:
		resm = requests.get("http://kplant.biodiv.tw/" + plantname + "/m/" + plantname + "m.htm")
		resm.encoding = resm.apparent_encoding
		page = pq(resm.text)
		page_content = page('a').text().split(u' ')
		for x in page_content:
			data.append("http://kplant.biodiv.tw/" + plantname + "/m/" + x + ".jpg")
			picname.append(x)
			# print x
		# for x in data:
		# 	print x

		# return req, data, plantname, picname
	except:
		print "error: " + url
	return req, data, plantname, picname

def imagecrawler(imgfilename, plantfilename, url, picturename):
	rx = requests.get(url, stream=True)
	temppath = imgfilename + '/' + plantfilename
	if not(os.path.exists(imgfilename + '/' + plantfilename)):
		os.makedirs(imgfilename + '/' + plantfilename)
	if rx.status_code == 200:
		with open(temppath + '/' + picturename + ".jpg", 'wb') as f:
			rx.raw.decode_content = True
			shutil.copyfileobj(rx.raw, f)
			f.close()

	return temppath   	
# def imagecrawler(imgfilename, plantfilename, url, picturename):
# 	# try:
# 	data = urllib.urlopen(url)
		
# 	if not(os.path.exists(filename + "/" + plantname)):
# 		os.makedirs(filename + "/" + plantname)
		
# 	temppath = filename + "/" + plantname + "/" + picname + ".jpg"
#     f = open(temppath, 'wb')
#     	# f = open(filename + '/' + plantname + "/" + picname + ".jpg", 'wb')
    	
#     f.write(data.read())
#     f.close()

#     return temppath
	# except:
	# 	return 1, temppath