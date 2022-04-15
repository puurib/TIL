![image-20220414153359799](C:%5CUsers%5Cstar3%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220414153359799.png)

![image-20220415042005989](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415042005989.png)

* POST와 POST가 아닐 때
* POST가 중요한 이유는 POST만 db를 조작함, GET은 db터치 x

* 설명할 수 있어야함

---

# 0406 수요일 Django Form

## 이전 복습 model

![image-20220414154647127](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154647127.png)이렇게 3가지로 정리할 것 

> model을 쓰는 이유? 사용자의 인풋을 받아서 db에 저장하려고

> modelform : 재사용성이 높아짐

---

## django model (웹 어플리케이션에서 데이터를 구조화하고 조작하기 위한 도구)

* model을 통해서 데이터베이스의 구조, 장고의 클래스를 정의했었다.
* `중요 !` model하나가 테이블 하나에 매핑됨
* mode과 DB는 다른 개념임
  * model을 통해서 레이아웃을 짜고, model을 기반으로 db를 생성함
  * DB : 체계화된 데이터의 모임
* 쿼리 : 데이터를 조회, 조작하기 위한 명령어
* 장고를 쓸 때는 sql을 직접 사용하지 않고 orm을 통해서 파이썬 문법으로 db와 소통했다.



> 데이터베이스의 기본 구조

* 스키마 : 데이터베이스의 자료의 구조
* 열 : 컬럼, 필드 , 속성
* 행 : 로우, 레코드 , 튜플



> orm

* orm : 객체 지향 매핑 (파이썬, db는 파이썬을 이해할 수 없음!)
  * 객체지향언어을 사용해서 호환되지 않은 데이터를 변환하는 프로그래밍 기법
  * = 파이썬을 사용해서 호환되지 않는 시스템 django와 sql간의 원활한 데이터 변환 프로그래밍 기술 
* django는 내장 orm을 사용함



> django orm

데이터베이스와 웹어플리케이션 소통을 sql로 할 수 없기 때문에 파이썬을 사용하고 orm이 sql로 해석을 하고 돌아오는 sql명령문을 파이썬 형태로 만들어준다.

![image-20220414154722584](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154722584.png)

* 요청을 보냄 queryset API : queryset API문법에 근거하여 python 객체지향적 표현으로 요청을 보냈다.
* 응답을 줌 object, queryset 객체으로 줬음 `이거 시험에 나왔었는데.. ㅎ`
  * 단일 객체 (object)
  * 단일 객체가아니라면 queryset 데이터 목록으로 줌



> orm 의 장점과 단점 `생산성 때문에 씀!`

장점 : sql을 잘 알기 못해도 db 조작이 가능하고, 객체 지향적 접근으로 높은 생산성

단점 : orm으로 완전한 서비스를 구현하기 힘들다.

-----> 현대 웹 프레임워크의 요점은 웹 개발의 생산성이 주요 포인트여서 사용하는 것



## orm의 사용이유 : DB를 객체(object)로 조작하기 위해 사용하는 것



`다시 model로 돌아와서`

## model (여기서 중요한 것은 코드를 어떻게 작성했냐 기억해내)

![image-20220414154815081](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154815081.png)

* models.py에 클래스 형태로 작성
* `models.Model`클래스를 상속 받아 서브클래스로 표현했다.
  * models모듈에 Model이라는 클래스가 있었다.
  * 예전에 장고 github에 들어가서 Model이 어떻게 되어있는지 살펴봤었음
  * model의 역할을 하는 부모 클래스라고 생각하면됨
  * 우리는 필드만 작성하면 됨
* 우리는 제목, 내용이라는 필드를 작성함, 필드는 각 데이터베이스의 열에 매핑
* id필드는 장고가 알아서 작성해주기 때문에 작성하지 않아도 됐다.
* ![image-20220414154836270](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154836270.png)models 모듈안에 Model필드로 존재하는 CharField, TextField가 있었음
  * 문자열 필드

    * CharField : 길이 제한 있는 text / max_length 필수 속성
    * TextField : 길이 제한 없는 text

---

## `model에서 가장중요` migrations

* migrations : django가 model에 생긴 변화를 반영하는 방법

필수 명령어 2가지 (코드 순서 지키기)

* `makemigrations`로 설계도를 만들고 `migrate`로 db에 반영
* migrate이후 모델과 db의 스키마가 동기화를 이뤘다고 보면 됨

![image-20220414154931548](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154931548.png)

곁다리

* sqlmirate : orm을 통해 sql 구문이 어떻게 사용되었는지 볼 수 있음
* showmigrations : 마이그레이션 파일들이 migrate 됐는지 안됐는지

![image-20220414155021546](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155021546.png)

![image-20220414155041135](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155041135.png)



* migrations/0001_initial.py 는 이렇게 생김

![image-20220414155610444](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155610444.png)

* 데이터베이스 입장에서는 이 설계도를 이해할 수 없어서 orm이 변경해주는 것이고
* 우리는 이 설계도에 수정을 가할 필요가 없다



> $ python manage.py migrate

![image-20220414155632420](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155632420.png)

* 이 명령어로 db에 실제 table이 생성됨



> sqlmigrate

![image-20220414155701756](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155701756.png)

> showmigrations

![image-20220414155726471](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155726471.png)

![image-20220414155742262](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155742262.png)

* 장고를 실행하는데 있어서 우리가 만든 앱 말고 기본 앱이 존재 한다.

  * project> settings.py> `INSTALLED_APPS` 에 기본앱이 존재함

    ![image-20220414155813906](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155813906.png)



>  model을 수정하자 (작성시간, 수정시간)을 추가하자

![image-20220414155841886](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155841886.png)

* auto_now_add , auto_now 시험나옴 ㅋ
* DateTimeField

* 수정하고 나서, makemigrations, migrate



> 왜 그냥 수정이 안되지?!

![image-20220414155908546](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155908546.png)



> 그럼 두번 째 설계도는 어떻게 될까 ? (변경사항 수정된)

dependencies에 첫번째 설계도가 들어있음

![image-20220414155938385](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414155938385.png)



> migration 3단계

![image-20220414160020929](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160020929.png)

## (중요) Database API (DB를 조작하기 위한 도구)

![image-20220414160055585](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160055585.png)

* 모델을 만들면 자연스럽게 매니저가 따라 붙음

![image-20220414160116878](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160116878.png)

![image-20220414160128593](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160128593.png)

## CRUD

* 조회
  * [] : 대괄호여서 리스트를 쓰듯이 조작하면 된다. 이터러블한 객체로 인덱싱, 슬라이싱 가능
  * ![image-20220414160201792](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160201792.png)

### create

> create 3가지 방법

1. 첫번째 방법

![image-20220414160932965](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160932965.png)



2. 두번째 방법 `이 방식을 고수하는 게 유효성 검사를 중간에 작성하기 위함`

![image-20220414160918057](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160918057.png)



![image-20220414160436050](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160436050.png)



3. 애초에 인스턴스를 생성하지 않고, 쿼리셋api 중에 create api를 사용함

`save 과정이 포함되어 있음`

![image-20220414160456659](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160456659.png)



> create 관련 메서드

![image-20220414160520435](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160520435.png)



### read

* 새로운 쿼리셋을 받는 것 : all / 쿼리셋을 주지 않음 : get (단일 객체 조회)

![image-20220414160553378](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160553378.png)

* get()은 쿼리셋을 주지 않고 단일 객체를 조회한다. 

![image-20220414160614265](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160614265.png)

* filter()  / get과는 다르게 쿼리셋을 반환함, 반환이 없어도 오류가 나지 않음

![image-20220414160631770](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160631770.png)

### update

* 조회를 먼저하고 저장을 꼭 해야 한다.

![image-20220414160647165](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160647165.png)



### delete

* 조회를 해서 저장을 함. 

![image-20220414160705370](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160705370.png)



### field lookups : 조회 시 특정 조건을 지정

* pk__gk = 2 : pk가 2보다 큰 거만 조회하겠다
* content__contains='ja' : ja가 포함된 거만 조회하겠다

![image-20220414160727384](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160727384.png)

## VIEW함수 

![image-20220414160751764](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414160751764.png)

* view에서 쿼리셋을 조회하고, 그걸 context에 키 : 벨류 형태로 받음
* render에 3번째 인자로 넘겨주면 사용할 수 있음



`articles/index.html`

### DTL

`{{  }}` : 변수

`{%  %}` : 태그

![image-20220414161141718](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414161141718.png)



* request에서 요청
  * request.POST까지만 하면 딕셔너리 형태여서 get을 사용해서 특정 값을 가지고 와야함.
  * title, content는 model에서 온게 아니라 input의 name값에서 온 것 

![image-20220414161233939](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414161233939.png)



## Redirect

* 페이지를 랜더링해서 보여주는 형태
* redirect가 되돌리기라는 것 같이 느껴지지만,
  * create함수가 동작해서 NEW에서 DETAIL로 간것
  * 로그는 2줄을 추가함
  * 제출을 누르는 순간 create로 요청을 보냄(초록색 POST)
  * 그 다음에 detail 요청 (redirect로 보낸 요청)
  * redirect는 뒤로가기라고 생각할 수 있지만 새로운 요청이 다시 가는 것
  * 글쓰고 우리가 직접 요청을 넣어줄 수 없으니, redirect로 요청을 넣은 것

![image-20220414161853767](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414161853767.png)![image-20220414161903980](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414161903980.png)

![image-20220414161726868](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414161726868.png)





---

## 0406 진도 Intro

* 우리는 지금까지 HTML form, input을 통해서 사용자로부터 데이터를 받음

* 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시함
* 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 함
  * ![image-20220414162343309](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414162343309.png)
* 이렇게 사용자가 입력한 데이터를 검증하는 것을 '유효성 검증'이라고 하는데, 코드 구현시 많은 노력이 필요한 작업이다. ---> 불필요해
* Django는 이러한 과중한 작업과 반복 코드를 줄여줌으로써 이 작업을 훨씬 쉽게 만들어 줌
  * Django Form



---

## Django Form

![image-20220414162500069](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414162500069.png)

* form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어수단
* Django는 From과 관련된 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공하여, 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함
* Django는 form에 관련된 작업의 아래 세 부분을 처리해줌
  * 렌더링을 위한 데이터 준비 및 재구성
  * 데이터에 대한 HTML form 생성
  * 클라이언트로부터 받은 데이터 수신 및 처리

---

## `Form의 핵심` Form Class

* Django Form 관리 시스템의 핵심
* Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field에 관련된 에러 메세지를 결정
* Django는 사용자의 데이터를 받을 때 해야할 과중한 작업(데이터 유효성 검증, 필요 시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등) 과 반복 코드를 줄여줌



## Form 선언하기 (crud 구현되어 있는 2번 프로젝트로 시작)

* 폴더 및 구조

![image-20220414164519616](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414164519616.png)![image-20220414164624898](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414164624898.png)

![image-20220414154048604](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220414154048604.png)

1. 가상환경 구축하기

```bash
$ python -m venv venv
```

2. 가상환경 실행시키기

```bash
$ source venv/Scripts/activate 
```

3. interpreter 변경하기

ctrl+shift+p 로 ![image-20220407092513578](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220407092513578.png)

가상환경 설정

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

![image-20220407100047982](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220407100047982.png)

``` bash
$ pip freeze > requirements.txt
```

---

## Forms.py

* 앱에 forms.py를 생성함

![image-20220415021058443](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415021058443.png)

* models.py와 forms.py는 비슷하지만 model의 title은 models모듈에서 가지고 온것이고, forms title은 forms 모듈에서 가지고 온 것
* 이름은 같지만 같은 필드는 아님
* forms.py에서 Charfield의 속성인 max_length는 필수 인자가 아니다 !

``` python
from django import forms # 내장 폼 import

# import했던 forms모듈의 form 클래스를 부모 클래스로 상속함
# 모델과 굉장히 유사
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField() # Charfield의 속성인 max_length는 필수 인자가 아니다 !
```



### 기존의 form, input 태그를 대체해보자 (new, update page)

* views.py를 고침 (new, update)

``` python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

from .forms import ArticleForm #  명시적 상대경로를 씀


def new(request):
    form = ArticleForm()  # ArticleForm 으로 form 인스턴스 생성
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```



* new.html 의 form과 input을 고칠려고함

  ![image-20220415022243186](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022243186.png)

  

![image-20220415022143216](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022143216.png)

![image-20220415022500400](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022500400.png)

``` html
<!-- new.html-->

{% extends 'base.html' %}


{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}                    <!-- {{ form.as_p }}  이 부분 -->
    <input type="submit">
  </form>
  <hr>

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

![image-20220415022252905](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022252905.png)

![image-20220415022445252](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022445252.png)



* models에서 ![image-20220415022628281](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022628281.png)max_length를 10으로 줘봐야, 실제 input창에서는 10자 이상 들어갔었지만,
* form에서 쓴 max_length는 10자 이상 써지지 않음![image-20220415022826820](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415022826820.png)

* 오해하면 안되는 부분은 사용자로부터 10자만 받을 수 있는지는 아직 모름, 유효성 검사를 view에서 해봐야함

* 10자 이상 써지지 않는다는데 10자만 받을 수 있는지는 아직모른다는게 무슨뜻이야?
* 그런데 content는 model에서는 textfield였는데, form에서는 그런 자동완성이 뜨지 않는다. 그럼 textfield는 쓸 수없는건가? 





### from rendering options

![image-20220415023235341](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415023235341.png)

* 예 ) {{form.as_p}}![image-20220415023313550](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415023313550.png)p태그로 나뉘어있음



### form

![image-20220415023507884](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415023507884.png)

![image-20220415024021379](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415024021379.png)

![image-20220415023736663](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415023736663.png)

``` python
from django import forms # 내장 폼 import

# import했던 forms모듈의 form 클래스를 부모 클래스로 상속함
# 모델과 굉장히 유사
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea) # 위젯 사용, 이렇게 하면 태그가 textarea로 바뀜
    #content = forms.CharField(widget=forms.PasswordInput) # 이러면 태그는 password
```

* django widget 로 찾아서 위젯 컨트롤



### form field choicefield

![image-20220415023948633](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415023948633.png)

원래대로라면

![image-20220415024244814](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415024244814.png)

이렇게 썼을 텐데 {{form.as_p}}로만 표현되어 있어서  forms.py에 써야하니까! 

공식문서를 보자! 2개 이상의 튜플을 넣어야함

![image-20220415024339650](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415024339650.png)



``` python
# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.Form):
    # 대문자는 choicefield의 스타일 가이드
    REGION_A = 'sl'
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGION_D = 'gm'
    REGION_F = 'bu'
    # 하나의 리스트로 묶고 2개 이상의 튜플로 묶음
    # 첫번째 : 변수값(value), 두번째 : 사용자에게 출력되는 형태 
    # 만약 사용자가 서울을 클릭하면 우리한텐 sl이 넘어온다
    REGIONS_CHOICES = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
        (REGION_C, '광주'),
        (REGION_D, '구미'),
        (REGION_F, '부울경'),


        title = forms.CharField(max_length=10)
        content = forms.CharField(widget=forms.Textarea)
        region = forms.ChoiceField(choices=REGIONS_CHOICES)
        # 초이스필드는 select이 기본값이라 위젯을 략해도 된다.
		#region = forms.ChoiceField(widget=forms.Select, choices=REGIONS_CHOICES)
```

![image-20220415024647342](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415024647342.png)![image-20220415024820414](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415024820414.png)

* django coding style 문서 확인 해보기



### 여러개 출력 CheckboxSelectMultiple

* 위젯만 바꿔줌

![image-20220415025204166](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025204166.png)

![image-20220415025115965](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025115965.png)

![image-20220415025150663](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025150663.png)





## ModelForm (이미 만들어져있는 모델에 맞춰서 form을 설정)

### Intro

* 이미 모델 필드에 쓰여져있는 필드를 사용하는 건 중복될 수 있음

![image-20220415025407965](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025407965.png)



### ModelFrom Class

![image-20220415025525580](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025525580.png)



### ModelForm Class 선언하기

![image-20220415025702030](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025702030.png)

* 메타 데이터 : 데이터를 위한 데이터![image-20220415025814106](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415025814106.png)



* forms.py

``` python
from django import forms
from .models import Article # [2] import


class ArticleForm(forms.ModelForm):
    # [3] 필드 정의 안해도 되네??
    
    class Meta:
        model = Article          # [1] 무슨 모델 기반으로 만들건데?? 
        fields = '__all__'
        # fields와 exclude(제외하겠다)는 동시에 사용 불가
        # exclude = ('title',)  

```

* fields 개별로 쓰기 ![image-20220415030034317](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415030034317.png)
* fields 다 받기 ![image-20220415030102429](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415030102429.png)
* 필드 정의도 안하고, 위젯으로 textfield로 안했는데 알아서 다해줬어..
  * created_at, updated_at은 애초에 사용자 입력 받는 대상이 아니라 출력에서도 빠져있다.

---

* 결과

![image-20220415030142282](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415030142282.png)





## form과 modelform 차이 (상황과 역할에 따라 씀)

* form - 로그인 (db에 저장안될 때 )

  * 로그인할 때, db에 저장하는 게 아니라 내부적인 인증 과정만 거칠 것임

  * 단순히 데이터로서만 사용될 때

    

* modelform - 회원 가입 (db저장이 필요할 때)

  * db에 저장하는 구조 



* 필수 : not null
* 선택 : null





## ModelForm이 쉽게 해주는 것 

![image-20220415030942171](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415030942171.png)

* 2번의 경우 ![image-20220415031011767](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415031011767.png) 원래는 이런식으로 데이터를 받는데, 격변이 일어날 것임 (지금은 어떤 값이 건 다 받음)





## Model 

* 현재 ArticleForm으로 데이터를 받고 있음

![image-20220415031226894](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415031226894.png)

``` python
def create(request):
    # ArticleForm()으로 form 인스턴스를 만드는데,
    # 그 안에 request.POST안에 모든 딕셔너리 형태의 데이터가 들어있으니 통째로 받음
    form = ArticleForm(request.POST)
    
    # 만약에 form 메서드중에 is_valid() 매서드 (ArticleForm()의 인스턴스 매서드)를 호출하면,
    # ArticleForm의 데이터(request.POST)의 유효성 검사를 하고,
    # is로 시작한다면, return값이 boolean임
    if form.is_valid():  # 유효성 검사
        # 유효성 검사를 통과했다면 저장해. (=글작성이 됐다면)
        # form.save()로 생성된 객체를 article로 받아줌 
    	article = form.save()
        # 통과되면 detail로 보내자
        return redirect('articles:detail', article.pk)
    
    	# 에러 
        #print(form.errors)
    # 통과X되면 다시 그 페이지 보여줌
    return redirect('articles:new')
```



* 하나하나 다 받지 않고,<img src="0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415031424996.png" alt="image-20220415031424996" style="zoom:50%;" /> 
* request.POST안에 모든 딕셔너리 형태의 데이터가 들어있으니 통째로 받음
* 유효성 검사를 진행함 (max_length 10자넘으면 유효성검사에서 탈락됨)

### is_valid()

![image-20220415033113781](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415033113781.png)

![image-20220415033309801](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415033309801.png)



* form.errors
* ![image-20220415033418199](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415033418199.png)

![image-20220415033354838](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415033354838.png)





##  create, update

* instance = article 값의 유무로 create, update가 갈림

![image-20220415033518544](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415033518544.png)



new : html 랜더링, 모델 폼 제공해서 데이터 받고 create를 호출함

create : post요청만 받음

![image-20220415034741067](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415034741067.png)



## new와 create를 합쳐서 c를 만듦

``` python

```

![image-20220415035205340](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035205340.png)



![image-20220415035514567](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035514567.png)

![image-20220415035619664](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035619664.png)

``` python
# 최종 형태

def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():  # 유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
        # print(form.errors)
    else:
    # new
        form = ArticleForm()
    context = {
        'form': form,      #이부분의 form은 1. 유효성 검사를 통과못한 것 (에러메세지를 들고있음)
                           #2. 그냥 사용자 입력 받지 않은 빈 form
    }
    return render(request, 'articles/create.html', context)
```

* 여기서 contect의 상황
  * 1. 유효성 검사를 통과못한 것 (에러메세지를 들고있음)
    2. 그냥 사용자 입력 받지 않은 빈 form



![image-20220415035827825](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035827825.png)

* NoReverseMatch : 해당되는템플릿 url을 봐야함
* 에러메세지가 랜더링된다.
* ![image-20220415035944871](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035944871.png)

![image-20220415035933038](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415035933038.png)



* 2번 상황

![image-20220415040014877](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415040014877.png)

![image-20220415040159711](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415040159711.png)

* 액션이 없으면 현재 url로 요청을 보냄
* but 명시적으로 쓰는 것을 권장 ![image-20220415040231260](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415040231260.png)





## update

![image-20220415040425352](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415040425352.png)

* edit : 기존 데이터 조회
* update : POST

``` python
def update(request, pk):
    # 한번만 작성 article = Article.objects.get(pk=pk)
    article = Article.objects.get(pk=pk)
    # article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # update [2]
        # article = Article.objects.get(pk=pk)
        # instance=article 이 값이 있어야함
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():  # 유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # edit [1]
        # article = Article.objects.get(pk=pk) 중복이여서 맨 위 한번 만 함
        # instance=article 이 값이 있어야함
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

```





## delete (단독 페이지가 없음) 수정할 필요 x

![image-20220415040117017](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415040117017.png)



``` python

```





## form modelform 비교

![image-20220415041426653](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041426653.png)

![image-20220415041754480](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041754480.png)

![image-20220415041659797](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041659797.png)

매핑을 꼭 해주어야함



## forms.py 파일 위치

![image-20220415041500802](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041500802.png)





## widgets 활용하기

![image-20220415041528786](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041528786.png)

![image-20220415041552679](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041552679.png)



* 모델 폼이지만, 결국 또 필드를 정의 (커스텀)
  * 클래스는 공백으로 구분됨
  * 부트스트랩은 클래스에 지정해야함
  * ![image-20220415042546246](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415042546246.png)

![image-20220415041559315](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415041559315.png)

``` python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
            }
        ),
        # 들여쓰기 주의 (위젯과 같은 단)
        error_messages={
            'required': 'Please enter your content!!!',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```







----

## Rendering fields manually

* django Rendering fields manually![image-20220415043246608](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043246608.png)
* ![image-20220415043301812](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043301812.png)

![image-20220415043009658](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043009658.png)



1. Rendering fields manually

![image-20220415043057671](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043057671.png)



``` html
{% extends 'base.html' %}


{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>

  <h2>1. Rendering fields manually</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <input type="submit">
  </form>
  <hr>
  <h2>2. Looping over the form’s fields</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form %}
      {% if field.errors %}
        {% for error in field.errors %}
          <div class="alert alert-warning">{{ error }}</div>
        {% endfor %}
      {% endif %}
      {{ field.label_tag }}
      {{ field }}
    {% endfor %}
    <input type="submit">
  </form>

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}

```



2. Looping over the form’s fields

![image-20220415043319834](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043319834.png)





## bootstrap 사용

![image-20220415043510780](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043510780.png)



![image-20220415043421618](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043421618.png)

![image-20220415043544124](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043544124.png)

![image-20220415043437333](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043437333.png)

![image-20220415043559093](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043559093.png)



![image-20220415043632754](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043632754.png)

![image-20220415043640827](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043640827.png)

![image-20220415043736300](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043736300.png)



2. 두번째 방법

![image-20220415043754068](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043754068.png)

![image-20220415043808458](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043808458.png)

* 앱등록까지 해야한다

![image-20220415043845633](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043845633.png)



![image-20220415043821746](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20Django%20Form%20PPT%20%EC%A0%95%EB%A6%AC.assets/image-20220415043821746.png)



커스텀보단 정해져있는걸로..

```html
<!-- update.html -->

{% extends 'base.html' %}
<!-- load --> 

{% load bootstrap5 %}


{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
      <!-- load --> 
    {% bootstrap_form form %}
    {% comment %} {{ form.as_p }} {% endcomment %}
    <input type="submit">
  </form>
  <a href="{% url 'articles:detail' article.pk %}">back</a>
{% endblock content %}
```



---------------------------

