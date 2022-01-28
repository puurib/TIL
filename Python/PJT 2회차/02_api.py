# 0. import
import requests

# 1. URL 및 요청변수 설정
# https://api.themoviedb.org/3/movie/now_playing?api_key=e53010cbbbc91dcb3b26e8894f6a8116&region=KR&language=ko
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'

params = {
    'api_key' : 'e53010cbbbc91dcb3b26e8894f6a8116',
    'region' : 'KR',
    'language' : 'ko'
}

# 2. 요청 보낸 결과 저장
# tmdb는 json으로 준다...그래서 .json()을 사용할 수 있음
response = requests.get(BASE_URL+path, params=params)
# 3. 조작..
print(response.url)
data  = response.json()

print(type(data)) # dictD
print(data.keys()) # dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results'])
print(type(data.get('results'))) # list
print(data.get('results')[0]) # list 의 첫번째 구조 = dict
print(len(data.get('results'))) # 20개