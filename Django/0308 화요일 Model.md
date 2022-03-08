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

