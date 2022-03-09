# 0308 화요일 Model

![image-20220308091712263](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308091712263.png)

* sql자체가 쿼리문을 쓰는 것



### database의 기본 구조

* 스키마: 설계도 같은 것

![image-20220308091855882](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308091855882.png)



## ORM

* model을 사용해서 객체를 만들고 database로 접근하겠다.





## DB의 종류

* 테이블이 있는 sql
* 테이블이 느슨한 nosql --> 채팅, 빠르게 변하는 데이터들

![image-20220308093531690](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308093531690.png)

* 단점 : orm은 효율이 조금 떨어짐
* 그러나 개발속도가 높아짐으로  orm을 사용한다.

![image-20220308094011434](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308094011434.png)





## 새 프로젝트 생성

![image-20220308095116535](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308095116535.png)



* settings.py에 앱 등록



### models.py

![image-20220308101840836](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308101840836.png)

* id를 생성해주지 않으면 자동으로 만들어짐





`#필드`

* null과 blank

null은 db에 저장될때 해당 필드가 빈값이 될지 말지 (모든 필드는 기본적으로 널값이 허용되진 않는다.)

blank는 db와 연관없고, 해당 필드를 비워둘지 말지를 설정



* charfield는 반드시 max_length 지정이 필요하다





## migrations

![image-20220308103340365](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308103340365.png)



* 마이그래이션 생성

``` bash
$ python manage.py makemigrations
```



* 마이그래이트하기

``` bash
$ python manage.py migrate
```



![image-20220308103205913](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308103205913.png)

* 아무것도 안해도 기본으로 한번은 migrate를 해줘야하는데, 그 이유는 기본 db도 이때 적용되기 때문이다.

![image-20220308103153973](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308103153973.png)



* orm이 sql로 변환한 것이 나옴

```bash
$ python manage.py sqlmigrate articles 0001
```

![image-20220308103625634](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308103625634.png)



* 

``` bash
$ python manage.py showmigrations
```

노란색 - 앱

초록색 - 마이그래이션

분홍색(X) - 적용된 것

![image-20220308104015090](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308104015090.png)



### auto_now_add , auto_now

![image-20220308104930866](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308104930866.png)

만들고 또 반영하면 이전에 데이터가 있었을 수 도 있으니 이런 것들이 뜨게 된다.

![image-20220308105247982](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308105247982.png)

여기서 1번을 선택하면 default값을 주면서 생성이 되고

2번은 그만두고 내가 추가해보겠단 의미.. 새로 생성된 것들에 직접 default값을 추가해주면된다

지금 현재로선 1번! (현재날짜시간을 default값으로 만들어줌)



![image-20220308105218861](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308105218861.png)







## ORM은 모델을 객체로 해서 사용한다

![image-20220308110759944](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308110759944.png)



## ORM 사용

![image-20220308112920750](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308112920750.png)



* 장고의 모든 기능을 사용할 수 있는 shell (여기서 orm이 사용가능)

``` bash
$ python manage.py shell
```



![image-20220308110854887](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308110854887.png)



* articles앱 안에 models.py의 Article 클래스를 가져와라

![image-20220308111051829](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111051829.png)

* 모든

![image-20220308111137392](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111137392.png)

![image-20220308111618012](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111618012.png)

 article은 Article()로 만들어진 비어있는 객체 자체에서 title, content를 넣을 수 있음



* 이 그림처럼 만들건데, save를 해야함

![image-20220308111558596](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111558596.png)



```shell
>>> article = Article.objects.all()[0]
>>> article.title
'첫번째 글'
>>> article.content
'첫번째 글이라고~'
```



* 저장 후 데이터 불러옴

![image-20220308111818141](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111818141.png)

![image-20220308111938621](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111938621.png)

![image-20220308111947339](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308111947339.png)



* 2번째 방법

![image-20220308112127646](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308112127646.png)

```shell
>>> article = Article(title="두번째 글", content="점심머먹징?")
>>> article.save()
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```



* 3번째 방법 : save없이 만드는법

![image-20220308112253093](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308112253093.png)

``` shell
>>> Article.objects.create(title="세번째 글", content="살빼야하는데")  
<Article: Article object (3)>
```





### `__str__`

![image-20220308131126395](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308131126395.png)

![image-20220308131216995](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308131216995.png)







### `django-extensions`

* 설치

``` bash
$ pip install django-extensions
```

* 패키지 등록 (앱, 패키지, 장고 기본내장 순으로) 
  * `django_extensions` 언더바 주의.. 설치할때는 대시이면서..ㅋㅋ

![image-20220308132015789](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308132015789.png)



* 실행

``` bash
$ python manage.py shell_plus
```



* ipython 설치 (얘는 등록안해줘도 됨)

``` bash
$ pip install ipython
```







### `shell_plus`

![image-20220308132436685](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308132436685.png)



``` shell
In [3]: article_1= Article.objects.all()[0]

In [4]: article_1.id
Out[4]: 1

In [5]: article = Article.objects.get(id=1)

In [6]: article.title
Out[6]: '첫번째 글'

In [7]: Article.objects.create(title="첫번째 글", content="실제로는 네번째 글")
Out[7]: <Article: 첫번째 글>

In [8]: Article.objects.all()
Out[8]: <QuerySet [<Article: 첫번째 글>, <Article: 두번째 글>, <Article: 세번째 글>, <Article: 첫번째 글>]>


```



* get() : PK와 써줌 (여러개인 값을 찾으면 에러남)

``` shell
In [9]: Article.objects.get(title="첫번째 글")  # 에러남
```

![image-20220308133638043](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308133638043.png)

*  PK와 씀

![image-20220308134040745](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308134040745.png)



### `filter`


![image-20220308134019280](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308134019280.png)

![image-20220308134149667](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308134149667.png)

``` shell
In [10]: articles = Article.objects.filter(title="첫번째 글")

In [11]: articles
Out[11]: <QuerySet [<Article: 첫번째 글>, <Article: 첫번째 글>]>
```





### filte(조건) : 조건을 `lookup`으로 부름

![image-20220308134938013](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308134938013.png)

* `filter documents`

https://docs.djangoproject.com/en/3.2/ref/models/querysets/





* `현재 버전의 requirements.txt` 만들기

![image-20220308131704910](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308131704910.png)





### `update`

![image-20220308140825457](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140825457.png)

#### article이란 변수에 4번째를 가져와라

![image-20220308140438231](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140438231.png)



![image-20220308140445152](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140445152.png)

변경



![image-20220308140526736](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140526736.png)

잘 바뀜

![image-20220308140545523](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140545523.png)



### `delete`

![image-20220308140656458](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140656458.png)

맨 뒤가 사라짐

![image-20220308140708257](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308140708257.png)







## admin-superuser 생성

``` bash
$ python manage.py createsuperuser
```



![image-20220308141605348](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308141605348.png)



## admin.py에 등록

![image-20220308141943029](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308141943029.png)





### 실습

![image-20220308142642184](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308142642184.png)



### 하는 방법

1. 프로젝트 urls.py

![image-20220308144210503](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308144210503.png)

* 16줄 주의
* include를 넣어서 모든 urls를 불러옴

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
]
```



2. 앱의 urls.py

![image-20220308144253314](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308144253314.png)

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
]
```



3. 앱의 views.py

![image-20220308144353947](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308144353947.png)

``` python
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')
```





4, 프로젝트에 base.html

![image-20220308144926991](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308144926991.png)



5. 프로젝트 settings.py에 등록

`디렉터리 구조 주의` 프로젝트 하위가 아니라 동일선상에 `templates` 폴더를 두어야함

![image-20220308145000959](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308145000959.png)



7. index.html

![image-20220308150825814](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308150825814.png)



---





### (실습) views.py에서 models.py의 정보를 가지고 오기



![image-20220308150706651](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308150706651.png)

---

### 하는 법

1. print()로 찍어봄 -> 밑에 잘 나오는지 확인 (터미널)

![image-20220308152938507](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308152938507.png)





2. 템플릿으로 이 코드를 넘김

![image-20220308153021760](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308153021760.png)





3. 템플릿

![image-20220308153306599](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308153306599.png)

* 교수님 코드

![image-20220308160650038](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308160650038.png)

---

## 글쓰기=form 만들기

![image-20220308154247407](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308154247407.png)

* 완성

![image-20220308155133603](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308155133603.png)

``` html
{% extends 'base.html' %}
{% block content %}

  <h1 class="text-center"> new article </h1>
  <form action="">
    <!--lable의 for와, input의 id는 짝꿍-->
    <!--input의 name은 서버로 보낼 때 필요-->
    <label for="title"> Title : </label> 
    <input type="text" id="title" name="title">
    <br> <!--줄바꿈 breaking line-->
    <label for="content"> Content : </label>
    <br>
    <textarea name="content" cols="30" rows="5" id="content"> </textarea>
    <br>
    <input type="submit">
  </form>

  <a href="/articles/index/">목록보기 </a>
{% endblock content %}
```





## url 이름으로 넣기

![image-20220308155314292](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308155314292.png)





* 템플릿에서 이렇게

![image-20220308155431585](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308155431585.png)





---

## 글쓴걸 받기 (request)

* form의 action값 수정

![image-20220308161923938](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308161923938.png)



### views.py

* views.py 수정 (create) --> form에서 name에 title, content로 적어줬기 때문에 받아오기 가능

![image-20220308161819566](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308161819566.png)





* 프린트 찍히는 거 확인

![image-20220308161952438](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308161952438.png)





* 데이터에 저장하기

분홍색 : model에 있는 field명

초록색 : 입력된 데이터 변수

![image-20220308162648515](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308162648515.png)







#### 순서 지정

* 가져온다음에 최신순으로 정렬

![image-20220308163152032](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308163152032.png)



* pk로 정렬해서 가져와

![image-20220308163450628](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308163450628.png)





* 최신순으로 가져와 `-pk`

![image-20220308163533734](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308163533734.png)





## http method

get : 가져올 때 (url querystring으로 보냄)

post : body 내에 넣어서 보냄

![image-20220308163955542](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308163955542.png)



* new.html에서 method수정

![image-20220308165042459](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308165042459.png)

``` html
{% extends 'base.html' %}
{% block content %}

  <h1 class="text-center"> new article </h1>
  <form action="{% url 'articles:create' %}" method="POST">
    <!--method="POST", csrf_token은 짝꿍-->
    {% csrf_token %}
    <!--lable의 for와, input의 id는 짝꿍-->
    <!--input의 name은 서버로 보낼 때 필요-->
    <label for="title"> Title : </label> 
    <input type="text" id="title" name="title">
    <br> <!--줄바꿈 breaking line-->
    <label for="content"> Content : </label>
    <br>
    <textarea name="content" cols="30" rows="5" id="content"> </textarea>
    <br>
    <input type="submit">
  </form>

  <!--<a href="{/articles/index/}">목록보기 </a>-->

  <a href="{% url 'articles:index' %}">목록보기 </a>
{% endblock content %}
```





* views.py 수정

![image-20220308165306933](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308165306933.png)





## method="POST" 

## csrf 토큰 (a.k.a 글 천개 쓰고 그런 도배 방지)

![image-20220308164713653](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308164713653.png)



![image-20220308164901346](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308164901346.png)

* 장고가 알아서 검증해줌

![image-20220308165206541](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308165206541.png)







## 글쓰고 바로 거치지 않고 넣기.

* 템플릿을 랜더하는게 아니라, index처리하는 url로 보내면 됨

1. redirect 추가

![image-20220308170025667](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308170025667.png)





2. url을 사용함 (not 템플릿)

![image-20220308170105112](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308170105112.png)





* 잘나옴

![image-20220308170222376](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308170222376.png)





### 정리하자면, 호출 -> db저장 -> redirect

![image-20220308170308952](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308170308952.png)



* 동일 기능을 했던 create.html은 지워도됨 (작성완료 됐다는 걸 알려주는 페이지)







----

![image-20220308170923502](0308%20%ED%99%94%EC%9A%94%EC%9D%BC%20Model.assets/image-20220308170923502.png)