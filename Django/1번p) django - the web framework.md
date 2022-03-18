# 1번ppt) Django - the web framework

https://edu.ssafy.com/edu/lectureroom/openlearning/openLearningView.do#none;

## 목차



### Django

>Django is high-level python web framework that encourages rapid development and clean, pragmatic design. It takes care of much of hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.
>
>Django는 빠른 개발과 깨끗하고 실용적인 디자인을 장려하는 고급 python 웹 프레임워크입니다. 웹 개발의 번거로움을 많이 덜어주기 때문에 번거로운 작업 없이 앱 작성에 집중할 수 있습니다.



## Web framework

* Django

* web(world wide web)
* static web page (정적 웹 페이지)
* dynamic web page (동적 웹 페이지)
* 정적 웹 페이지 vs 동적 웹 페이지

* framework (Application framework)
* web framework 



#### ✅ Django를 사용해야 하는 이유 

* 검증된 python 언어 기반의 web framework, 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨



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

* 앱 등록 (INSTALLED_APPS에 등록) - 반드시 생성 후 등록 (꼭)
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



#### 3. Templates

* template 파일 경로 기본 값 : app폴더 안의 template 폴더로 지정



#### 4. 추가 설정

* LANGUAGE_CODE
* TIME_ZONE
* USE_I18N
* USE_L10N
* USE_TZ



## Template



## HTML Form



## URL



















