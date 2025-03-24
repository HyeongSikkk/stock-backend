import requests
import pandas as pd
from datetime import datetime
import time

class DataCrawler :
    MAX_RETRIES=10
    
    def __init__(self) :
        self.target_url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
        self.header= {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "111",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "_ga=GA1.1.563907863.1742392029; __smVisitorID=jB4ighSQF42; _ga_808R2EHLL3=GS1.1.1742392079.1.1.1742393362.0.0.0; _ga_Z6N0DBVT2W=GS1.1.1742816533.2.1.1742816559.0.0.0",
            "Host": "data.krx.co.kr",
            "Origin": "http://data.krx.co.kr",
            "Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201040101",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.set_payload()
    
    def set_payload(self) :
        self.time_update()
        today_datetime= f"{self.now.year}{self.now.month}{self.now.day}"
        self.payload= {
            "bld":"dbms/MDC/STAT/standard/MDCSTAT01501",
            "locale":"ko_KR",
            "mktId":"ALL",
            "trdDd":today_datetime,
            "share":"1",
            "money":"1",
            "csvxls_isNo":"false",
        }
    
    def time_update(self) :
        self.now= datetime.today()
    
    # krx에 현재 주식 데이터 요청
    def req_post_krx(self) :
        for _ in range(self.MAX_RETRIES) :
            is_success=False
            try :
                res= requests.post(self.target_url, data=self.payload, headers=self.header)
                res.raise_for_status()
                data= res.json()
                pd.DataFrame(data).to_csv(f"./data/{self.now.hour}{self.now.minute}.csv", index=False)
                is_success=True
            except :
                continue
            if is_success :
                break
            
    
    def check_hour(self) :
        hour= self.now.hour
        minute= self.now.minute
        if 9 <= hour <= 16 and minute % 5 == 0:
            return True
        return False
    
    def run(self) :
        while True :
            # 시간값 업데이트
            self.time_update()
            
            if self.check_time() :
                self.req_post_krx()
                time.sleep(60)

if __name__ == "__main__":
    data_crawler= DataCrawler()
    data_crawler.req_post_krx()