# ============ Set ============

# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymysql
from datetime import datetime


# 변수 지정
standard_time, ncnt_people, visit, all_visit = 0, 0, 0, 0



# ============ Function ============ 
def check():
  global ncnt_people, standard_time
  with open("nCnt.txt", "r") as file:
      for line in file.readlines():
        info_list = line.split("/")
        ncnt_people = info_list[0]
        standard_time = info_list[1]
        print("\n", line,"\n")

def sql_recorder(Now_people, Now_Time):
  conn = pymysql.connect(host="127.0.0.1", user="root", password="MySQLhelena5863*", db="nCntDB", charset="utf8")
  cur=conn.cursor()
  cur.execute("CREATE  TABLE userTable (people_num INT, time char(30))")
  cur.execute("INSERT INTO userTable VALUES('{0}', '{1}')".format(Now_people, Now_Time))
  conn.commit()
  conn.close()

# ============ Machine ============ 

# 웹 출력    
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

sql_recorder(int(ncnt_people,str(standard_time))) 

@app.get("/", response_class=HTMLResponse)
async def Page(request: Request):#, ncnt_people: str, current_time: str, standard_time: str):
    check()
    current_time = datetime.now()  # 실시간 시간 측정 
    current_time = str(current_time)[0:21]  # 필요한 부분 가공
    return templates.TemplateResponse("new.html", {"request": request, "counting": ncnt_people, "time": current_time, "old_time": standard_time})  # FastAPI로 new.html에 변수 값 전달

@app.get("/nCnt")
async def nCnt():
  check()
  current_time = datetime.now()  # 실시간 시간 측정
  current_time = str(current_time)[0:21]  # 필요한 부분 가공
  print(ncnt_people)
  return {"counting": ncnt_people, "time": current_time, "old_time": standard_time}