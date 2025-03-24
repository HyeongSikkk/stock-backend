import requests

req_url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
headers= {
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
payload= {
    "bld":"dbms/MDC/STAT/standard/MDCSTAT01501",
    "locale":"ko_KR",
    "mktId":"ALL",
    "trdDd":"20250324",
    "share":"1",
    "money":"1",
    "csvxls_isNo":"false",
}
res= requests.post(req_url, data=payload, headers= headers)
print(res.json().keys())