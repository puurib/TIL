import random
import requests
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def index(request):
    
    #return HttpResponse("<h1>hola :) </h1>")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice',
    }
    context = {
        'foods':foods,
        'info':info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발','햄버거','치킨', '초밥']
    pick = random.choice(foods)
    context= {
        'foods':foods,
        'pick':pick,
    }
    return render(request, 'articles/dinner.html', context)

#def dtl_practive(request):
#    return render(request, )

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message=request.GET.get('message')
    context = {'message':message}
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    print(name, "#######")
    return render(request, 'articles/hello.html', {'name':name})

def intro(request, name, age):
    context = {
        'name':name,
        'age':age
    }
    return render(request, 'articles/intro.html', context)

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'

    # 1. 이번 회차 당첨 정보 받아오기
    response = requests.get(url)
    lotto = response.json()

    # 2. 번호 6개만 가져오기
    winner = []
    bonus = lotto['bnusNo']
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # 3. 당첨 횟수 기록하기 위한 dictionary 만들기
    win_rate = {'1등': 0, '2등': 0, '3등': 0, '4등': 0, '5등': 0, '꽝': 0}

    # 4. 로또 1000장 구매하고 각 당첨번호와 비교하기
    for i in range(1000):
        my_numbers = random.sample(range(1, 46), 6)

        # 5-1. 내 자동으로 산 복권 번호와 당첨번호 반복문으로 개수 비교
        matched = 0
        for num in my_numbers:
            if num in winner:
                matched += 1

        # 5-2. 교집합으로 개수 비교
        # matched = len(set(winner) & set(my_numbers))

        # 6. 당첨된 횟수 체크
        if matched == 6:
            win_rate['1등'] += 1
        elif matched == 5 and bonus in my_numbers:
            win_rate['2등'] += 1
        elif matched == 5:
            win_rate['3등'] += 1
        elif matched == 4:
            win_rate['4등'] += 1
        elif matched == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1

    context = {
        'winner': winner,
        'bonus': bonus,
        'win_rate': win_rate,
    }

    return render(request, 'articles/lotto.html', context)