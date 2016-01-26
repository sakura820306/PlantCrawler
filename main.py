# coding=UTF-8
from connectsql import *
from crawler import *
import os

def main():

	filename = "plantimg"

	if not(os.path.exists(filename)):
		os.makedirs(filename)

	[conn, cur] = connectdb()
	urlarray = select_onecoldata(cur, "datasource", "url")
	urlidarray = select_onecoldata(cur, "datasource", "DSID")
	# oidarray = selectdata(cur, ["object o", "datasource ds"], ["oid", "urlid"], "ds.dsid = o.urlid")

	for url in urlarray:
		print urlarray.index(url)
		print url[0]
		[isError, data] = webcrawler(url[0])
		tempoid = 0
		if isError == 1:
			insertdata(conn, cur, "ErrordataSource", ["dsid"], [urlarray.index(url)+1])
		else:
			# data.append(str(urlarray.index(url)+1))
			try:
				# for n in data:
				# 	print n
				insertdata(conn, cur, "object", ["cname", "ename", "sourceurl"], [data[0], data[1], url])
				tempoid = selectonedata(cur, "object", "max(oid)")
				insertdata(conn, cur, "plantall", ["pid", "sname", "familia", "originplace", "distribution", "application", "stem", "leaf", "flower", "fruit", "feature"], [tempoid[0][0] ,data[3], data[2], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]])
			except Exception, e:
				print e
				insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlarray.index(url)+1, 1])
		
		[isError, data, plantnames, names] = imgsource(url[0])
		# print isError
		if isError == 1:
			insertdata(conn, cur, "ErrordataSource", ["DSID", "type"], [urlidarray[urlarray.index(url)], 2])
		else:
			for index in range(len(data)):	
				# try:
				print "start to save " + data[index]
				# 	insertdata(conn, cur, "archive", ["aid", "url"], [, data[index]])
				# except:
				# 	insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlidarray[urlarray.index(url)], 4])
				
				if not(os.path.exists(filename + '/' + plantnames)):
					os.makedirs(filename + '/' + plantnames)
		
				try:
					print "start to craw " + names[index] + ".jpg"
					filepath = imagecrawler(filename, plantnames, data[index], names[index])
					insertdata(conn, cur, "archive", ["oid", "filename", "fliepath", "source"], [tempoid[0][0], names[index], filepath, data[index]])
				except Exception, e:
				# except:
					print e
					# raise e
					insertdata(conn, cur, "ErrorimgSource", ["ISID"], [index+1])

			# try:
			# 	for index in englishname:
			# 		insertdata(conn, cur, "EnglishName", ["oid", "ename"], [urlarray.index(url)+1, index])
			# except:
			# 	insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlarray.index(url)+1, 2])

			# try:
			# 	for index in othername:
			# 		insertdata(conn, cur, "OtherName", ["oid", "cname"], [urlarray.index(url)+1, index])
			# except:
			# 	insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlarray.index(url)+1, 3])

	# if not(os.path.exists(filename)):
	# 	os.makedirs(filename)

	# for url in urlarray:
	# 	print urlarray.index(url)
	# 	print url[0]
	# 	[isError, data, plantnames, names] = imgsource(url[0])
	# 	# print isError
	# 	if isError == 1:
	# 		insertdata(conn, cur, "ErrordataSource", ["DSID", "type"], [urlidarray[urlarray.index(url)], 2])
	# 	else:
	# 		for index in range(len(data)):	
	# 			try:
	# 				print "start to save " + data[index]
	# 				insertdata(conn, cur, "imgSource", ["oid", "url"], [oidarray[urlidarray[urlarray.index(url)]][0], data[index]])
	# 			except:
	# 				insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlidarray[urlarray.index(url)], 4])
				
	# 			if not(os.path.exists(filename + '/' + plantnames)):
	# 				os.makedirs(filename + '/' + plantnames)
		
	# 			try:
	# 				print "start to craw " + names[index] + ".jpg"
	# 				filepath = imagecrawler(filename, plantnames, data[index], names[index])
	# 				insertdata(conn, cur, "imgData", ["IDID", "filepath", "filename"], [index+1, filepath, names[index]])
	# 			# except Exception, e:
	# 			except:
	# 				# raise e
	# 				insertdata(conn, cur, "ErrorimgSource", ["ISID"], [index+1])

			# for index in range(len(data)):
			# 	if not(os.path.exists(filename + '/' + plantnames)):
			# 		os.makedirs(filename + '/' + plantnames)
			# 	[isError, filepath] = imgcrawler(filename, plantnames, data[index], names[index])
			# 	if isError == 1:
			# 		insertdata(conn, cur, "ErrorimgSource", ["isid"], [urlarray.index(url)+1])
			# 	else:
			# 		try:
			# 			insertdata(conn, cur, "imgSource", ["oid", "url", "filepath", "filename"], [urlarray.index(url)+1, data[index], filepath, names[index]])
			# 		except:
			# 			insertdata(conn, cur, "ErrorSQL", ["dsid", "errortable"], [urlarray.index(url)+1, 4])

	closedb(conn,cur)

if __name__ == '__main__':
	main()