# coding=UTF-8
import psycopg2

conn_host='localhost'
conn_database='twplant_v1.2'
conn_user='postgres'
conn_password='postgres'
dbdata = 'host=' + conn_host + ' dbname=' + conn_database + ' user=' + conn_user + ' password=' + conn_password

conn = psycopg2.connect(dbdata)
cur = conn.cursor()

cur.execute("select t.tid, p.words from phrase p, Token t where p.words = t.words and p.type = 7 and p.kind = 3 order by Length(p.words) desc")

tidarray = []
wordarray = []

for tid in cur:
	tidarray.append(tid[0])
	wordarray.append(tid[1])

for index in xrange(len(tidarray)):
	cur.execute("INSERT INTO class(type) values (3);")
	conn.commit()
	
	cur.execute("SELECT max(cid) FROM class;")
	tempcid = cur.fetchall()

	cur.execute("update class set cname=%s, idpath=%s, namepath = %s where cid = %s;", (wordarray[index], '1/5/33/'+str(tempcid[0][0]), '首頁/果實/種子/'+wordarray[index], tempcid[0][0]))
	conn.commit()

	oidarray = []
	cur.execute("select d.oid from DupIndex d, phrase p, Token t, object o where p.words = t.words and d.tid = t.tid and o.oid = d.oid and p.type = 7 and t.tid = "+str(tidarray[index]))
	for index_co in cur:
		oidarray.append(index_co[0])
	for index_co in oidarray:
		cur.execute("INSERT INTO co(cid, oid) values (%s, %s);", (tempcid[0][0], index_co))
		conn.commit()

	print 'Insert: ' + wordarray[index] + ' OK!'

cur.close()   
conn.close()