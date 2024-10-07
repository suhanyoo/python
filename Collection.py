import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=삼성전자',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
global result 
result = []

def Naver():
    try:
        # 뉴스 관련도순 기사 10개 
        top_10 = soup.select('#main_pack > section.sc_new.sp_nnews._fe_news_collection._prs_nws > div.api_subject_bx > div.group_news > ul > li')
        i = 0
        for x in top_10:
            i += 0
            # 뉴스 제목, 본문 , 언론사 , 게시날짜
            Newstitle = x.select_one('.bx > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit')
            NewsBody = x.select_one('.bx > div.news_wrap.api_ani_send > div > div.news_contents > div > div > a')
            NewsCompany = x.select_one('.bx > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press')
            NewsTime = x.select_one('.bx > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > span')
            NewsHref = x.select_one('.bx > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit')
            NewsHref = NewsHref["href"]

            NewResult = {
                '번호':i,
                '제목':Newstitle.text,
                '본문':NewsBody.text,
                '언론사':NewsCompany.text,
                '게시날짜':NewsTime.text,
                '링크':NewsHref
            }
            result.append(NewResult)
    except Exception as e:
        print("Error 발생 {e}")

def get_Result():
    return result