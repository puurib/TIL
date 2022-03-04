import random
from django.shortcuts import render
from django.http import HttpResponse
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