# 웹 사이트의 정보를 가지고 오고 싶다.
import requests
from bs4 import BeautifulSoup

# 1-1. 주소 
URL = 'https://finance.naver.com/sise/'
# 1-2. 요청
# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# response (200) : 성공적으로 가져왔다! 404 / 500
response = requests.get(URL).text 
# print(type(response)) # type : string

# 2-1. BeautifulSoup (text -> 다른 객체)
# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# HTML 파일에 있는 데이터를 가져오기 위해서 활용 
data = BeautifulSoup(response, 'html.parser')
# print(type(data), type(response)) # <class 'bs4.BeautifulSoup'> <class 'str'>

# 2-2. 내가 원하는 정보를 가져온다!
# 선택자 (selector)
kospi = data.select_one('#KOSPI_now')
print(kospi.text)