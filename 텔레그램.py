from urllib import response
import requests
from requests.models import Response
from bs4 import BeautifulSoup
import datetime
from datetime import date,timedelta
import telegram
import time
from apscheduler.schedulers.blocking import BlockingScheduler


용산="0013"

nowday=(datetime.date.today().isoformat())

token_id="5081033456:AAFC9HDCGCdGyvKe2inpuxkHfKSV7Ab1Rww"

chat="1054405622"



area_code='01'#서울
theather='0013' #용산

def check_4dx():
    url=f"http://www.cgv.co.kr/theaters/?areacode=01&theaterCode={용산}&date=" 
    today = datetime.date.today().strftime("%Y%m%d")
    url+=today
    print(url)
    response=requests.get(url)
    bs=BeautifulSoup (response.text,'html.parser')
    chatbot=telegram.Bot(token=token_id)

    result=[]

    nullvalue = '[<strong>\r\n                                                '
    nullvalue2 = '</strong>]'

    fordx= bs.find_all('div',attrs={"class":"col-times"})
    chatbot.sendMessage('test0')
    if(fordx):
        for i in fordx:
            if (i.find(class_='forDX')):
                title=i.select('a>strong')
                result.append(str(title))
        result=[word.replace(nullvalue, '')for word in result]
        result=[word.replace(nullvalue2, '')for word in result]
        print (result)
        for movie in result:
            chatbot.sendMessage(chat_id=chat,text=movie +"의 4dx오픈")
            sc.pauese(0) #blocking schedule
            chatbot.sendMessage("test1")

    else:
        chatbot.sendMessage(chat_id=chat,text="아직 오픈전")
        chatbot.sendMessage("test2")

sc=BlockingScheduler(timezone='Asia/Seoul')
sc.add_job(check_4dx,'interval',seconds=30)

sc.start()
