# 0412 account 계정

장고 오픈 소스 auth

https://github.com/django/django/blob/main/django/contrib/auth/models.py

---

## 가상환경 및 세팅

1. 가상환경 구축하기

```bash
$ python -m venv venv
```



2. 가상환경 실행시키기

```bash
$ source venv/Scripts/activate 
```

3. interpreter 변경하기

ctrl+shift+p 로 ![image-20220407092513578](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407092513578.png)

가상환경 



4. `.gitignore` 파일 생성 후 

   gitignore.io 사이트에서 python, window, django, visual studio code 등을 넣어서 생성 후

   파일에 넣고 저장



5. pip list로 목록 확인하기

```bash
$ pip list
```



6. 버전에 맞는 `django` 설치

```bash
$ pip install django==3.2.10
```

6-1. `requirements.txt` 설치

* 재귀(리컬시브) 사용

``` bash
$ pip install -r requirements.txt
```



7. 패키지 설치했다면

![image-20220407100047982](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407100047982.png)

``` bash
$ pip freeze > requirements.txt
```



---

## 프로젝트 시작

1. 프로젝트 시작하기 (프로젝트 이름은 django_auth)

```bash
$ django-admin startproject django_auth .
```



2. git init 

![image-20220412091252917](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412091252917.png)

3. 앱 생성 (앱 이름은 accounts)

```bash
$ python manage.py startapp accounts
```

4. 프로젝트의 settings.py 의 `INSTALLED_APPS`에 앱 추가 (순서 주의)

* 코드 컨벤션 
  * 장고가 기본적으로 만든 것 위에 app을 넣어줌
  * 장고는 위에서 부터 먼저 찾는다.

![image-20220407093643677](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407093643677.png)



5. 프로젝트의 settings.py 시간, 언어 설정

* 타임존 바꾸기 (기본으로 이정도만)

![image-20220407094042341](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407094042341.png)



![image-20220407093703923](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407093703923.png)



6. 기본 db ㅊㅅ기

![image-20220412091744688](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412091744688.png)







![image-20220412092053784](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412092053784.png)

![image-20220412092102048](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412092102048.png)

![image-20220412092147737](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412092147737.png)

![image-20220412092250364](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412092250364.png)



1. 기본 구조

![image-20220407101154663](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407101154663.png)





2. base.html에 

* block 만들기
* 부트스트랩 cdn 가져오기

base.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django Auth</title>
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
</html>
```

3. settings.py에 저장하기
   * 커서를 올린 채 ctrl 누르면, 경로가 보임

![image-20220407101445477](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220407101445477.png)





---

## signup

urls.py

![image-20220412093005881](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412093005881.png)



VIEW

* 장고 제공 기본 유저 모델 사용
  * from django.contrib.auth.models import User

* 

![image-20220412093602872](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412093602872.png)

![image-20220412093555085](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412093555085.png)





이렇게 새로운 객체를 만들면 인스턴스가 생성됨 

![image-20220412093702209](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412093702209.png)

![image-20220412093844296](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412093844296.png)





* 액션생략시 내 자신에게 다시 보냄
* type="password" 은 동글뱅이로 나오는 역할 

``` html
{% extends 'base.html' %}

{% block content %}
  <!--action="" 은 생략과 같다-->
  <form action="" method="POST">
    {% csrf_token %}
    
    <label for="username"> 유저네임: </label>
    <input type="text" id="username" name="username"><br><br>

    <label for="password"> 비밀번호: </label>
    <input type="password" id="password" name="password"><br><br>

    <button type="submit">가입하기</button>
  </form>

{% endblock content %}
```





다하고 ![image-20220412094515993](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094515993.png) auth_user에 들어가면 

데이터가 있음

터가![image-20220412094505343](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094505343.png)



장고오픈소스 들어가면

![image-20220412094648838](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094648838.png)

이거 view에서 설정해준거 



![image-20220412094805204](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094805204.png)

AbstractUser에 상속받고 있음

얘를 클릭하면 들어갈 수 있음 

![image-20220412094856234](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094856234.png)

필드

![image-20220412094927984](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094927984.png)

![image-20220412094940046](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412094940046.png)



패스워드 자체를 암호화해서 저장

![image-20220412095117066](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412095117066.png)







---

## login

* url

``` python
from django.urls import path
from . import views

app_name= 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'), # 회원가입
    path('login/', views.login, name='login'), # 로그인
]
```

* view

![image-20220412101803811](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412101803811.png)

``` python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login # 유저가 일치하면 유저객체반환, 불일치 none반환
from django.contrib.auth.forms import UserCreationForm
```

임포트함



![image-20220412101534684](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412101534684.png)

로그인을 하면 세션에 세션데이터를 새롭게 생성하고, 브라우저로 줘야함

![image-20220412101614236](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412101614236.png)



![image-20220412102128046](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412102128046.png)

``` python
# 로그인 POST 방식 제외하고 무시(index페이지로 보내거나, 새로고침)
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # User.objects.get(username=username)이 인증과정을 장고에서 함수로 지원함
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #로그인 진행
            auth_login(request, user) # 이렇게 하면 자동으로 세션만들고 쿠키만들고 리턴해줌
            return redirect('accounts:index')
        else:
            # 잘못입력한 경우 -> 에러
            error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'

    else: # POST가 아닌 모든 경우
        error_message = ''
    
    context = {
        'error_message' : error_message
    }

    return render(request, 'accounts/login.html', context)
```







html

``` html
{% extends 'base.html' %}

{% block content %}
  <h1> login </h1>  
  <!--action="" 은 생략과 같다-->
  <form action="" method="POST">
    {% csrf_token %}
    
    <label for="username"> 아이디: </label>
    <input type="text" id="username" name="username"><br><br>

    <label for="password"> 비밀번호: </label>
    <input type="password" id="password" name="password"><br><br>

    <button type="submit">로그인</button>
  </form>
  {{error_message}}
{% endblock content %}
```







----

# form을 사용한 리뉴얼



https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.forms

![image-20220412103557359](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412103557359.png)



form

![image-20220412103709610](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412103709610.png)







> view에 넣기

![image-20220412103759114](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412103759114.png)





> signup 수정

이전

![image-20220412104226604](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104226604.png)

수정 후 

![image-20220412104207581](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104207581.png)



>  html

이전

![image-20220412104258565](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104258565.png)

이후

![image-20220412104445034](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104445034.png)



화면

![image-20220412104432090](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104432090.png)





## 회원가입 > 자동 로그인 > 메인 페이지

## ![image-20220412104510689](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104510689.png)

![image-20220412104708348](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104708348.png)

이걸하면 로그인처리가 됐었음 15~17번줄

![image-20220412104920700](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412104920700.png)



---

# 로그인처리 폼

* import하기 (AuthenticationForm  추가)

``` python
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login # 유저가 일치하면 유저객체반환, 불일치 none반환
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
```

![image-20220412105145708](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412105145708.png)



* 수정전 

![image-20220412105659314](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412105659314.png)



* 장고폼 사용 (수정 후 )

  * 내코드

  ![image-20220412111516787](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412111516787.png)

  * 교수님 코드

![image-20220412105612328](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412105612328.png)



* 로그인 페이지

![image-20220412105723906](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412105723906.png)







---

## 로그아웃 (세션 삭제)

1. url

![image-20220412110213399](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412110213399.png)



2. view

* import (로그아웃 추가)

``` python
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout # 유저가 일치하면 유저객체반환, 불일치 none반환
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
```

![image-20220412110647327](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412110647327.png)





3. index페이지에서 ![image-20220412110849957](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412110849957.png)

![image-20220412110911886](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412110911886.png)







4. 동작

   로그인하면 세션이 생김

![image-20220412110816656](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412110816656.png)

​	로그아웃하면 세션 사라짐





---

## cf) 미들웨어를 거쳐서, 들어왔다가 나감

![image-20220412111012334](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412111012334.png)

view에서 매번 사용하는 

request는 객체이고, 이 미들웨어가 request.user라는 속성을 추가해준다

로그인이되어있지 않은상태 = 세션이 없는 상태 = 쿠키에 세션이 없는상태라면

익명의 유저로 됨

---

로그인이 안된상태면 로그아웃이 안보여야지..!!이런거 처리해야함



---

로그인된 사람인지 아닌지 알게 하는 것

* view에서 추가하는 것



* index.

![image-20220412112242102](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412112242102.png)



---



![image-20220412130323202](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412130323202.png)

* request.GET.get('next') 가져오기

![image-20220412130434037](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412130434037.png)





---

* 회원탈퇴
  * `<int:pk>` 가 필요없는 이유는 유저정보이기 때문에..

![image-20220412130657964](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412130657964.png)



뷰

![image-20220412131008553](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131008553.png)

추가

![image-20220412131508690](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131508690.png)



이러면 포스트 요청이 아니여서 405 상태코드가 발생함

![image-20220412131151076](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131151076.png)



![image-20220412131231192](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131231192.png)



따라서 회원탈퇴는 form을 사용해야함

![image-20220412131353423](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131353423.png)







---

## 수정

![image-20220412131727748](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131727748.png)



> url







> view

* 폼 가져다쓰기(안써다되는데 쓰는게 편해서)

![image-20220412131934941](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412131934941.png)

* 원래 update는

![image-20220412132048713](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412132048713.png)

이런식이었음

![image-20220412132311243](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412132311243.png)





* html 생성

![image-20220412132354918](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412132354918.png)



다하면 

![image-20220412132651626](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412132651626.png)

이렇게 나오는데 상속해서 새로운 폼을 만들어야함



`forms.py`를 새로 만듦

![image-20220412132859664](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412132859664.png)

![image-20220412133014727](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412133014727.png)

여기서 모든 필드가 필요한게 아니여서 

재정의해줌

![image-20220412133204697](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412133204697.png)

![image-20220412133446944](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412133446944.png)

![image-20220412134026318](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412134026318.png)







> view

바인딩 폼 (데이터가 다 채워져있는)

![image-20220412134303691](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412134303691.png)



![image-20220412134051687](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412134051687.png)

![image-20220412134631801](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412134631801.png)









---



자동으로 url만 되어있음



![image-20220412134940085](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412134940085.png)

![image-20220412135236344](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412135236344.png)





![image-20220412135333269](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412135333269.png)





![image-20220412135855995](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412135855995.png)

결론 

![image-20220412140034593](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412140034593.png)





![image-20220412140418737](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412140418737.png)

![image-20220412140456584](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412140456584.png)

세션 무효화 방지

![image-20220412140657012](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412140657012.png)





![image-20220412140948864](0412%20account%20%EA%B3%84%EC%A0%95%20%EB%B3%B5%EC%8A%B5.assets/image-20220412140948864.png)

