# coding=UTF-8
import psycopg2
import time

conn_host='localhost'
conn_database='twplant_v1.2'
conn_user='postgres'
conn_password='postgres'
dbdata = 'host=' + conn_host + ' dbname=' + conn_database + ' user=' + conn_user + ' password=' + conn_password

conn = psycopg2.connect(dbdata)
cur = conn.cursor()

cur.execute("select pid from vd_dc_des where databyte is null")

pidarray = []

for pid in cur:
	pidarray.append(pid[0])

for pid in pidarray:
	cur.execute("select Tokenize(%s,%s)", (pid, 3))
	conn.commit()
	print 'Tokenize: ' + str(pid) + ' OK!'

# cur.execute("select tid, words from Token")

# tidarray = []
# wordarray = []

# for tid in cur:
# 	tidarray.append(tid[0])
# 	wordarray.append(tid[1])

# for tid in xrange(len(tidarray)):
# 	try:
# 		cur.execute("select CountSE(%s,%s)", (tidarray[tid], wordarray[tid]))
# 		conn.commit()
# 		print 'SE: ' + str(tidarray[tid]) + ' OK!'
# 	except psycopg2.Error, e:
# 		print tidarray[tid]
# 		print wordarray[tid]
# 		print e
# 		cur.close()   
# 		conn.close()
# 		conn = psycopg2.connect(dbdata)
# 		cur = conn.cursor()


cur.close()   
conn.close()