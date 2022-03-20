## 시험

* 시험범위: 교재 기준 django_01, django_02, homework, workshop 등
  단, 3월 14일 수업 내용 (SQL) 제외
* 시험유형: 객관식, 단답형 및 서술형으로 구성
* 알려준 문제 배점 총 28점 (탈락자는 없고 평균은 낮도록 출제)





.

---

[천기누설]

extends 

관리자 모델, 어드민, 

경로 app_name (언더바 빼먹으면  x)

데이터 정렬 order by

어드민 :  사이트.register

migrate 

오토나우에드, 

base_dir (대문자!!)

프레임워크에 대한 전반적인설명

장고 프레임워크 mtv 패턴 - 뭐였더라?

create superuser 

---

# 1번ppt) Django - the web framework

https://edu.ssafy.com/edu/lectureroom/openlearning/openLearningView.do#none;

## 목차

![image-20220320000809309](%EC%A0%95%EB%A6%AC)Django.assets/image-20220320000809309.png)



### Django

>Django is high-level python web framework that encourages rapid development and clean, pragmatic design. It takes care of much of hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.
>
>Django는 빠른 개발과 깨끗하고 실용적인 디자인을 장려하는 고급 python 웹 프레임워크입니다. 웹 개발의 번거로움을 많이 덜어주기 때문에 번거로운 작업 없이 앱 작성에 집중할 수 있습니다.

## Web framework

* Django
* web(world wide web)
* static web page (정적 웹 페이지)
  * 일반적으로 HTML, CSS, JavaScript로 작성됨
* dynamic web page (동적 웹 페이지)
* 정적 웹 페이지 vs 동적 웹 페이지
* framework (Application framework)
* web framework 



#### ✅ Django를 사용해야 하는 이유 

* 검증된 python 언어 기반의 web framework, 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨
* Django는 다소 독선적인 framework이다.



#### ✅ framework architecture 

#### = MVC design pattern (model-view-controller)

* 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
* Django는 MTV Pattern 패턴이라고 함



#### 💯 MTV Pattern (model)



#### ✅ MVC Pattern 과 MTV Pattern의 차이

* 어떤 식으로 동작하는 지





## ✅ Django intro

* Django 설치 전 가상환경 생성 및 활성화
* Django 설치
* 프로젝트 생성
  * 프로젝트 이름에는 Python , Django 에서 사용중인 키워드를 피해야 한다.
  * '-'(하이픈)도 사용할 수 없다.
  * ex) Django, text, class, django-test 등 
* Django 서버 시작하기(활성화)
* 메인 페이지 로켓 확인



* Application 생성 (복수형 권장)

* 앱 등록 (INSTALLED_APPS에 등록) 

  🌈반드시 생성 후 등록 (꼭) - INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음🌈

* `urls.py`

* `views.py`

* `templates`

* 

---

참고) LTS : Long Term Support (장기 지원 버전) - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책, 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함.

---

#### ✅ Project 과 Application의 차이



##### 프로젝트 구조

* `__init__.py`
* `asgi.py`
* `settings.py`
* `urls.py`
* `wsgi.py`
* `manage.py` : Django 프로젝트와 다양한 방법으로 상호작용하는 `command`라인 유틸리티



##### Application 구조

* `admin.py` : 관리자용 페이지를 설정하는 곳
* `apps.py` : 앱의 정보가 작성된 곳
* `models.py` : 앱에서 사용하는 model을 정의하는 곳
* `tests.py` : 프로젝트의 테스트 코드를 작성하는 곳
* `views.py` : view 함수들이 정의되는 곳





## 요청과 응답

#### 1. URLS



#### 2. View

* HTTP 요청을 수신하고, HTTP응답을 반환하는 함수 작성
* model을 통해 요청에 맞는 필요 데이터에 접근
* template에게 HTTP 응답 서식을 맡김



#### 3. Templates

* 실제 내용을 보여주는데 사용되는 파일
* 파일의 구조나 레이아웃을 정의 (ex:HTML)

* 🌈 template 파일 경로 기본 값 - app폴더 안의 template 폴더🌈로 지정



#### 4. 추가 설정

* LANGUAGE_CODE
* TIME_ZONE
* USE_I18N
* USE_L10N
* USE_TZ



## Template

* 데이터를 제어하는 도구이자 표현에 관련된 로직
* Django에서 사용하는 built-in template system (Django template language)



#### Django Template Language (DTL)

ppt내용 다시 볼 것

* 단순히 python이 HTML에 포함된 것이 아니며,
  🌈 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것🌈



#### ✅ DTL Syntax 4가지 (VFTC : Variable, Filters, Tags, Comments)

##### 1. Variable

> {{variable}}



##### 2. Filters :  60개의 built-in template filters를 제공

> {{variable`|filter`}}



##### 3. Tags : 약 24개의 built-in template tags를 제공

> {% tag %}

> {% if %} {% endif %}



##### 4. Comments

> 한 줄 주석 : {#           #}



> 여러 줄 주석 : 
>
> {% comment %}  
>
> 주석
>
> 주석
>
> {% endcomment %}



#### 🌈 코드 작성 순서 (데이터의 흐름에 맞추어 작성) 🌈 

* urls.py -> views.py -> templates 순



#### ✅ [실습] DTL Syntax (p58 ~ 63)



#### ✅ Template inheritance (템플릿 상속) - for 재사용성 

##### 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림 - 반드시 최상단에 작성

> {% extends '`부모템플릿.html`' %}



##### 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의, 즉 하위 템플릿이 채울 수 있는 공간

> {% block content %}  {% endblock %}



#### ✅ [실습] Template inheritance (p66 ~ 68)

1. app_name/templates 디렉토리 외 템플릿 추가 경로 설정



#### Template Tag - "include"

> {% include ' ' %}

* 템플릿을 로드하고 현재 페이지로 랜더링
* 템플릿 내에 다른 템플릿을 포함하는 방법



#### ✅ [실습] Template Tag - "include" (p70 ~ 71)



#### Django template system (feat. Django 설계 철학)

1. 표현과 로직(view)를 분리



2. 중복 배제





## HTML Form

#### HTML form element (핵심 속성 - action, method)



#### HTML input element (핵심 속성 - name, )



#### HTML label element 



#### HTML id attribute



#### HTTP



#### HTTP request method - GET



#### [실습] Throw & Catch (p83 ~ 84)





## URL

#### Django URLs

* Dispatcher(발송자,운항관리자)로서의 URL
* 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작 됨





#### Variable Routing

* url 주소를 변수로 사용하는 것
* url의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음



#### URL Path converters



#### [실습] Variable Routing (p90)



#### App URL mapping

* app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고,
  app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

* 🌈 이제는 각 app에 urls.py를 작성하게 됨 🌈



#### [실습] App URL mapping (p92 ~ 94)

* 각각의 앱 안에 urls.py를 생성하고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁



#### Including other URLconfs 

* include()

* 🌈 Django는 명시적 상대경로 (from .modul import ..)를 권장 🌈 
* 



#### Naming URL patterns



#### URL template tag

> { % url '  ' % }

* 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
* 템플릿에 URL을 하드 코딩하지 않고도
  DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법



#### [실습] URL template tag 적용하기 



---

# 2번ppt) Django2 - Django model

## 목차



## Model (웹 애플리케이션의 데이터를 🌈 구조화하고 조작 🌈하기 위한 도구)

* 단일한 데이터에 대한 정보를 가짐
* 저장된 데이터베이스의 구조(layout)
* Django는 model을 통해 데이터에 접속하고 관리
* 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨



#### Database

##### 데이터 베이스 (DB)

* 체계화된 데이터의 모임



##### 쿼리 (Query)

* 쿼리는 데이터를 조회하기 위한 명령어
* 조건에 맞는 데이터를 추출하거나 조작하는 명령어
* Query를 날린다 -> DB를 조작한다.



#### Database의 기본 구조

##### 스키마



##### 테이블







## ORM

* Object - Relational - Mapping



#### ORM의 장점과 단점

##### 장점



##### 단점



#### 왜 ORM을 사용할까? cuz 우리는 DB 객체를 조작하기 위해 ORM을 사용한다.



#### models.py 작성



#### 사용 모델 필드

##### CharField(max_length=None, ** options)



##### TextField(**options)





## Migrations

#### Migrations

##### Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어



#### [실습] makemigrations - migrate - DB table 확인 - sqlmigrate - showmigrations - 모델 수정 - makemigrations - 



#### DateField's options

##### auto_now_add



##### auto_now



#### DateTimeField가 아닌 DateField의 options를 확인한 이유



#### 반드시 기억해야 할 migration 3 단계

> 1. models.py

* model 변경 사항 발생 시



> 2. $ python manage.py makemigrations

* migrations 파일 생성



> 3. $ python manage.py migrate

* DB 반영 (model의 DB의 동기화)





## Database API : DB를 조작하기 위한 도구

#### DB API



#### DB API 구문 - Making Queries

> `Article.objects.all()`



#### DB API



#### Django shell



#### [실습] 라이브러리 등록 및 실행



## CRUD

#### CRUD 뜻



#### [실습] READ (p50 ~ 54)



#### CREATE 관련 메서드 

##### save() method 



##### str method



#### READ



#### [실습] READ



#### [실습] UPDATE



#### [실습] DELETE



#### Field lookups



#### QuerySet API





## Admin Site

#### Automatic admin interface



#### admin 생성

> $ python manage.py createsuperuser



#### 💯 admin 등록



#### ModelAdmin options



#### CRUD with views



#### HTTP method

##### GET



##### POST



#### 사이트 간 요청 위조 (Cross-site request forgery = CSRF)



#### csrf_token template tag



#### CsrfViewMiddleware



#### Django shortcut function - redirect()

> `앱이름`/views.py에 
>
> from django.shortcuts import render, redirect





#### Detail 



#### CRUD 실습

















