# coding=UTF-8
import psycopg2
from settings import *

def connectdb():
	conn = psycopg2.connect(dbdata)
	cur = conn.cursor()
	return [conn,cur]

def insertdata(conn,cur,table,col,data):
	tempstr = ""
	tempdata = ""
	for x in range(len(col)):
		if(x < (len(col)-1)):
			tempstr = tempstr + col[x] + ", "
			# tempdata = tempdata + "{" + str(x) + "}, "
			tempdata = tempdata + "%s, "
		else:
			tempstr = tempstr + col[x]
			# tempdata = tempdata + "{" + str(x) + "}"
			tempdata = tempdata + "%s"
	# "{1}, {0}".format('world', 'Hello')
	# tempdata = ""
	# for x in range(len(data)):
	# 	if(x < (len(data)-1)):
	# 		tempdata = tempdata + data[x] + ", "
	# 	else:
	# 		tempdata = tempdata + data[x]

	# print "INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");"
	# cur.execute("INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");")
	# sql = "INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");".format(data)
	cur.execute("INSERT INTO " + table + " (" + tempstr + ") VALUES (" + tempdata + ");", data)
	# cur.execute(sql)
	conn.commit()

def select_onecoldata(cur,table,col):
	cur.execute("SELECT " + col + " FROM " + table + ";")
	# cur.execute("SELECT " + col + " FROM " + table + " where dsid > 123;")
	return cur.fetchall()

def selectdata(cur,table,col,search):
	tempstr = ""
	for x in range(len(col)):
		if(x < (len(col)-1)):
			tempstr = tempstr + col[x] + ", "
		else:
			tempstr = tempstr + col[x]

	temptable = ""
	for x in range(len(table)):
		if(x < (len(table)-1)):
			temptable = temptable + table[x] + ", "
		else:
			temptable = temptable + table[x]

	cur.execute("SELECT " + tempstr + " FROM " + temptable + " WHERE " + search + ";")
	# cur.execute("SELECT url FROM datasource where dsid < 20;")
	return cur.fetchall()

def selectonedata(cur,table,col):
	# tempstr = ""
	# for x in range(len(col)):
	# 	if(x < (len(col)-1)):
	# 		tempstr = tempstr + col[x] + ", "
	# 	else:
	# 		tempstr = tempstr + col[x]

	# temptable = ""
	# for x in range(len(table)):
	# 	if(x < (len(table)-1)):
	# 		temptable = temptable + table[x] + ", "
	# 	else:
	# 		temptable = temptable + table[x]

	cur.execute("SELECT " + col + " FROM " + table + ";")
	# cur.execute("SELECT url FROM datasource where dsid < 20;")
	return cur.fetchall()

def closedb(conn,cur):
	cur.close()   
	conn.close()