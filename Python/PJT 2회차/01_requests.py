# 웹 사이트의 정보를 가지고 오고 싶다.
import requests
from bs4 import BeautifulSoup

# 1. 주소
URL = 'https://finance.naver.com/sise/'


# 2. 요청
#requests.get(주소)
'''
response = requests.get(URL)
print(response, type(response)) # => <Response [200]> <class 'requests.models.Response'>
'''

response = requests.get(URL).text # text를 붙이면 파일로 보여줌
print(response) # <Response [200]> : 정상적으로 가지고 왔다, 404 : 내 잘못, 500 : 개발자 잘못
print(type(response)) # => str



# 2-1.BeautifulSoup (text-> 다른 객체)
data = BeautifulSoup(response, 'html.parser')
print(data) # => str이 BeautifulSoup 객체로 바뀜

