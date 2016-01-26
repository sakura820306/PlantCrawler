# coding=UTF-8
import urllib2
import requests
from pyquery import PyQuery as pq
from connectsql import *

def main():
	kplant_crawler()

def kplant_crawler():
	res = requests.get("http://kplant.biodiv.tw/校園植物首頁.htm")

	res.encoding = 'utf-8'
	page = pq(res.text)
	# page.encoding = 'unicode'
	page_content = page('font').text()
	page_source = page_content.split(' ')
	# page_source_url = []

	page_removedata = [u"賽伯破布", u"鐵莧", u"蝦夷蔥", u"銀槭", u"銀樺", u"山茶花", u"樟樹", u"鵝仔草", u"白花深山野牡丹", u"檳榔", u"山苧麻", u"緬梔花", u"金鈴花", u"風鈴花", u"山枇杷", u"奇異果",
					u"香瓜梨", u"箭根薯", u"釋迦", u"更多", u"油加利", u"油柑", u"紫莓", u"紫莉草", u"菩提樹", u"幌菊", u"烏臼",
					u"囊萼花", u"烏來草", u"龍脷葉", u"龍眼", u"獨行菜", u"益智子", u"優曇華", u"濱刺草", u"檵木", u"繁蔞",
					u"尼泊爾籟簫", u"海紅豆", u"紫梅", u"魯冰花", u"川上氏薊", u"玉蘭花", u"茭白", u"筍", u"茴香", u"茶",
					u"茶匙癀", u"茶匙癀", u"茶匙黃", u"茯苓菜", u"薯蕷", u"黃菽草", u"釘錘果", u"黃獨", u"獨黃", u"川上氏木薑子",
					u"白", u"桕", u"黃槿", u"馬拉巴栗", u"馬㼎兒", u"烏柿", u"馬纓丹", u"青椒", u"菜椒", u"青葉楠", u"非洲小百合",
					u"高山翻白草", u"圓葉尤加利", u"圓葉節節菜", u"高山酢漿草", u"圓葉鱗始蕨", u"灰木", u"台灣朴樹", u"石韋", u"南湖大山倒提壺",
					u"假馬齒莧", u"猴耳", u"楓樹", u"榆樹", u"心葉溲疏", u"交讓木", u"斗六草", u"日本山桂花", u"轎竿竹", u"轎槓竹",
					u"日本杜英", u"光葉柃木", u"光葉石楠", u"鏈莢豆", u"日本前胡", u"霧社櫻", u"基尖葉野牡丹", u"垂榕", u"麗格海棠",
					u"日本楨楠", u"密花苧麻", u"腺花毛蓼", u"月桂", u"樹", u"月桂", u"葉鄧伯花", u"寶塔龍船花", u"芙蓉", u"恆春皂莢",
					u"菜豆", u"蒂牡丹", u"木油桐", u"木春菊", u"扁核木", u"聖誕椰子", u"木麻黃", u"蘋婆", u"舞草", u"木薯", u"檬果",
					u"木虌子0", u"毛冬珊瑚", u"多花紫藤", u"蘭花參", u"琉璃草", u"香瓜", u"馬薯", u"甜椒", u"毛柱杜鵑", u"尖尾鳳", u"蘭嶼厚殼桂",
					u"刺格", u"過江龍", u"酪梨", u"柳葉水簑衣", u"草玉鈴", u"異葉紅珠", u"雷公銃", u"疏花風輪菜", u"鐵刀木", u"灰木",
					u"葶藶", u"水仙百合", u"鐵包金", u"百部", u"鐵線草", u"鐵莧", u"水柳樹", u"竹柏", u"珍珠草", u"榕樹", u"羊帶來", u"槐樹",
					u"細葉零餘子", u"滿福木", u"漢葒魚腥草", u"欒樨", u"肉穗草", u"變葉木", u"船仔草", u"血桐", u"大水莞", u"水藍鈴", u"艾草",
					u"福滿木", u"豔紅鹿子百合", u"西印度櫻桃", u"紅豆杉", u"六倍利", u"翠芸草", u"欖仁樹", u"火焰百合", u"西洋蓍草", u"西洋椴樹",
					u"紅花三葉草", u"翠雲草", u"翠藍木", u"爪哇大青", u"紅花破布木", u"臺灣天南星", u"野胡桃", u"豔紫野牡丹", u"牛白藤",
					u"牛皮菜", u"牛膝菊", u"克魯茲王蓮", u"克育草", u"豔紅合歡", u"野牡丹葉冷水麻", u"菇", u"香青", u"舖地蜈蚣", u"臺灣", u"台東火刺木", u"十子木", u"台東柿",
					u"臺灣鼠麴草", u"刺葉王蘭", u"n"]

	del page_source [0:19]
	del page_source [len(page_source)-1]

	for index in range(page_source.count(u'\r\n')):
		page_source.remove(u'\r\n')

	for index in range(page_source.count(u'')):
		page_source.remove(u'')

	for index in page_removedata:
		page_source.remove(index)

	s = page_source.index(u')')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u'皮')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u'皮')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u'藤')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u'樹')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u'姑')
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	page_source.remove(u"山黃皮")

	s = page_source.index(u"檫樹")
	page_source[s] = u"台灣檫樹"

	s = page_source.index(u"燈籠椒")
	page_source[s] = u"風鈴辣椒"

	s = page_source.index(u"高山繡球藤")
	page_source[s] = u"高山藤繡球"

	s = page_source.index(u"心葉水薄荷")
	page_source[s] = u"伏生風輪菜"

	s = page_source.index(u"疏花苘麻")
	page_source[s] = u"淡紫紅花磨盤草"

	s = page_source.index(u"荷苞花")
	page_source[s] = u"荷包花"

	s = page_source.index(u"觀音竹(蓬萊竹)")
	page_source[s] = u"觀音竹"

	s = page_source.index(u"紅花石蒜石蒜")
	page_source[s] = u"紅花石蒜"

	s = page_source.index(u"灣二葉松")
	page_source[s-1] = page_source[s-1] + page_source[s]
	del page_source[s]

	s = page_source.index(u"咖啡")
	page_source[s] = page_source[s] + page_source[s+1]
	del page_source[s+1]

	s = page_source.index(u"紫菫")
	page_source[s] = page_source[s] + page_source[s+1]
	del page_source[s+1]

	s = page_source.index(u"芥藍")
	page_source[s] = page_source[s] + page_source[s+1]
	del page_source[s+1]

	s = page_source.index(u"臺灣")
	page_source[s] = page_source[s] + page_source[s+1]
	del page_source[s+1]

	spec_source = [u"芒果樹", u"虎葛", u"龍眼", u"雞兒腸", u"石竹(轎竿竹)", u"羅漢松", u"光蠟樹", u"密穗桔梗",
				u"麒麟花", u"彩色甘藍", u"合歡柳葉菜", u"扁蒲", u"指甲花", u"桶鉤藤", u"水柳",
				u"百眼藤", u"巒大杉", u"荷", u"福祿桐", u"紅花鼠尾草", u"王蘭"]

	spec_source_url = [u"http://kplant.biodiv.tw/" + spec_source[0] + u"/芒果.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[1] + u"/" + spec_source[1] + u"920529.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[2] + u"0/" + spec_source[2] + u".htm",
				   u"http://kplant.biodiv.tw/馬蘭/" + spec_source[3] + u".htm",
				   u"http://kplant.biodiv.tw/轎竿竹/石竹.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[5] + u"/" + spec_source[5] + u"920601.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[6] + u"/" + spec_source[6] + u"920706.htm",
				   u"http://kplant.biodiv.tw/尖瓣花/" + spec_source[7] + u".htm",
				   u"http://kplant.biodiv.tw/" + spec_source[8] + u"/" + spec_source[8] + u"-910716.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[9] + u"/page_01.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[10] + u"/合歡山柳葉菜.htm",
				   u"http://kplant.biodiv.tw/瓠子/" + spec_source[11] + ".htm",
				   u"http://kplant.biodiv.tw/" + spec_source[12] + u"/" + spec_source[12] + u"920528.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[13] + u"/台灣鼠李.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[14] + u"/" + spec_source[14] + u"-910716.htm",
				   u"http://kplant.biodiv.tw/雞眼藤/" + spec_source[15] + u".htm",
				   u"http://kplant.biodiv.tw/香杉/" + spec_source[16] + u".htm",
				   u"http://kplant.biodiv.tw/" + spec_source[17] + u"/" + spec_source[17] + u"920529.htm",
				   u"http://kplant.biodiv.tw/" + spec_source[18] + u"/" + spec_source[18] + u"-910716.htm",
				   u"http://kplant.biodiv.tw/朱唇花/" + spec_source[19] + u".htm",
				   "http://kplant.biodiv.tw/王蘭/刺葉王蘭.htm"]

	[conn, cur] = connectdb()			   

	for index in page_source:
		tempstr = ""
		if index in spec_source:
			tempstr = spec_source_url[spec_source.index(index)]
		else:
			tempstr = "http://kplant.biodiv.tw/" + index + "/" + index + ".htm"
		# page_source_url.append(tempstr)
		# print (tempstr)
		insertdata(conn, cur, "datasource", ["source", "url"], ["http://kplant.biodiv.tw/", tempstr])

	# res2 = requests.get("http://kplant.biodiv.tw/山茶花/茶花目錄.htm")
	# res2.encoding = 'big5'
	# page2 = pq(res2.text)
	# page_content2 = []
	# for index_row in range(3,18):
	# 	page_content2.append(page('body > table > tr:nth-child(' + str(index_row) + ') > td:nth-child(1)').text())
	# 	page_content2.append(page('body > table > tr:nth-child(' + str(index_row) + ') > td:nth-child(2)').text())
	# # print page_content
	# # print page_content2

	# for index_row2 in range(3,12):
	# 	page_content2.append(page('body > table > tr:nth-child(' + str(index_row) + ') > td:nth-child(3)').text())

	# del page_content2[2]

	# for index in page_content2:
	# 	tempstr = ""
	# 	tempstr = "http://kplant.biodiv.tw/山茶花/" + index + "/" + index + ".htm"
	# 	# page_source_url.append(tempstr)
	# 	# print (tempstr)
	# 	insertdata(conn, cur, "datasource", ["source", "url"], ["\'http://kplant.biodiv.tw/\'", "\'" + tempstr + "\'"])

	# closedb(conn,cur)

# 虎葛
# 龍眼
# 雞兒腸
# 石竹(轎竿竹)
# 羅漢松
# 光蠟樹
# 密穗桔梗
# 麒麟花
# 彩色甘藍
# 合歡柳葉菜
# 扁蒲
# 指甲花
# 桶鉤藤
# 柿子
# 水柳
# 百眼藤
# 巒大杉
# 荷
# 福祿桐
# 紅花鼠尾草

#主程式從這裡開始
if __name__ == '__main__':
	main()