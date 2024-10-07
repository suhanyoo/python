from Collection import Naver,get_Result
from datetime import datetime
import Collection
import numpy as np
import re
import datetime

def dc():
    df = Collection.Naver()
    News_Data = Collection.get_Result()
    for x in range(0,len(News_Data),1):
        # 본문 = 등호가 들어 갈 경우 제거 하는 부분 
        Newsbody = News_Data[x]['본문']
        Trim_NewsBody = Newsbody.strip()
        Equals_NewsBody = Trim_NewsBody[:1]

        if Equals_NewsBody == "=":
            NewsbodySlice = Newsbody[1:]
            Newsbody[x]['본문'] = NewsbodySlice
        
        # 날짜 일전, 시간전 , 분전 , 초전 , 주전일 때 값 변환
        current = datetime.datetime.now()

        NewsTime = News_Data[x]['게시날짜']
        Trim_NewsTime = NewsTime.strip()
        NewsTimeNumber = Trim_NewsTime[:1]

        if "일" in NewsTime:
            day_ago = current - datetime.datetime.timedelta(NewsTimeNumber)
            print("성공")

dc()