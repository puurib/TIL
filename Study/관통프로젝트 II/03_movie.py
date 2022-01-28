# 0. import
import requests
from pprint import pprint

# 1. URL 및 요청변수 설정
# https://developers.themoviedb.org/3/movies/get-now-playing
# http로 요청보낼거야, 주소가 있고 그 주소에 요청파라미터에 값이 있어!
# https://api.themoviedb.org/3/movie/now_playing?api_key=8854669b886a6c07c12ea947bcc2311d&region=KR&language=ko
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'region': 'KR',
    'language': 'ko'
}

# 2. 요청 보낸 결과 저장
response = requests.get(BASE_URL+path, params=params)
print(response.status_code, response.url)
data = response.json()

# print(type(data)) # dict
# print(data.keys()) # dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results'])
# print(type(data.get('results'))) # list
# pprint(data.get('results')[0]) # list 첫번째 구조
# print(type(data.get('results')[0])) # dict
# print(len(data.get('results'))) # 20개

