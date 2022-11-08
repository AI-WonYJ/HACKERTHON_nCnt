import requests
import pymysql

url = "http://114.71.48.94:8080/nCnt" # url 에 https 가 아닌 http 사용할 것

# def sql_recorder(Now_Time, Now_people):
# 	conn = pymysql.connect(host="127.0.0.1", user="root", password="sscc", db="nCntDB", charset="utf8")
# 	cur=conn.cursor()
# 	#   cur.execute("CREATE  TABLE numberTable (time char(30), people_num INT)")
# 	cur.execute("INSERT INTO userTable VALUES('{0}', '{1}')".format(Now_Time, Now_people))
# 	conn.commit()
# 	conn.close()
	
# conn = pymysql.connect(host="127.0.0.1", user="root", password="sscc", db="nCntDB", charset="utf8")
# cur=conn.cursor()
# cur.execute("CREATE  TABLE numberTable (datetime char(30), people_num INT)")
# conn.commit()
# conn.close()

data = requests.get(url).json()
time = data['time'][:11] + data['old_time']
old_time2 = time
print(time, data['counting'])
while True:
  data = requests.get(url).json()
  time = data['time'][:11] + data['old_time']
  if time != old_time2 :
    old_time2 = time
    print(time, data['counting'])
