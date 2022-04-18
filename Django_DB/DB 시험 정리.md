# Django MODEL

## 1) 기본 DB 개념

* model : 하나의 DB에 각각의 model이 매핑
* DB : 데이터의 집합
* 쿼리 : 데이터 조회 명령어 (조건에 맞는 데이터 추출)
* 스키마 : 자료구조, 제약 조건
* 테이블
  * 열 / 컬럼 / 필드 / 속성
  * 행 / 로우 / 레코드 / 튜플
* ORM : 객체지향언어를 사용해서 호환되지 않는 시스템(django-sql)간에 데이터 변환하는 프로그래밍 기술
* ORM의 장점 : 높은 생산성
* ORM의 단점 : ORM만으로는 완전한 서비스 구현 못함



* 명령어

``` bash
$ python manage.py makemigratiaons
$ python manage.py migrate
$ python manage.py sqlmigrate `app_name` `0001`
$ python manage.py showmigratiaons
```

* model
  * auto_now_add : 최초 생성 일자 (insert시 갱신)
  * auto_now : save시 갱신

``` python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # DateTimeField는 DateField의 서브클래스
```

* Database API : DB 조작도구
  * `classname. manager. QuerySet API`
  * Article.objects.all() : 레코드 하나면 인스턴스 / 여러개면 쿼리셋 리턴
* QuerySet : 데이터베이스로 부터 전달된 객체 목록
  * 0 or 1 or 여러개
  * 조회, 필터, 정렬 수행 가능



## 2) RDB 개념

* 키와 값들의 간단한 관계를 표 형태로 정리한 데이터 베이스
* RDBS : 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
* SQLite : 서버 형태가 아닌 파일 형식의 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스



* Sqlite Data Type
  * NULL
  * INTEGER
  * REAL : 소수점
  * TEXT
  * BLOB : 입력된 그대로 정확히 저장된 데이터 

* 권장 데이터 타입
  * INTEGER
  * REAL : double, float
  * TEXT
  * BLOB : no type 
  * NUMERIC : boolean, date, datetime 등



* sql 분류

![image-20220418062351817](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418062351817.png)



* 데이터 베이스 생성

``` sqlite
$ sqlite tutorial.sqlite3

# .은 sqlite 프로그램의 기능을 실행하는 것
sqlite> .database 
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
```

* select

``` sql
sqlite> SELECT * FROM examples;

# 열이 위치가 안맞음
sqlite> .headers on
sqlite> SELECT * FROM examples;

# 열 위치도 맞게!
sqlite> .mode column
sqlite> SELECT * FROM examples;
```

* 테이블 생성 및 삭제

``` sql
-- 테이블 생성
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
	name TEXT
	);
	
CREATE TABLE classmates (
	name TEXT,
    age INT,
    address TEXT
	);
	
	
# 생성한 스키마 보기
sqlite> .schema classmates
하면 아래가 보임
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
	name TEXT
	);
	
-- 테이블 삭제
DROP TABLE classmates;
```



* insert

``` sql
INSERT INTO 테이블이름(컬럼) VALUES(값);

INSERT INTO classmates(name, age) VALUES('홍길동', 23);

INSERT INTO classmates(name, age, address) VALUES('홍길동', 23, '서울');
# 모든 열에 데이터가 있으면 컬럼 명시 안해도됨
INSERT INTO classmates VALUES('홍길동', 23, '서울');

# sqlite는 PK를 작성하지 않으면 자동으로 증가하는 옵션으로 rowid 컬럼 정의
SELECT rowid, * FROM classmates;  

# not null설정
-- 테이블 생성
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
	);

# 이렇게 넣으면 스키마에 id를 직접 작성했기 때문에 자동으로 들어가지 않는다. id를 넣어야함
INSERT INTO classmates VALUES('홍길동', 23, '서울');
# id까지 넣어줘야함
INSERT INTO classmates VALUES(1, '홍길동', 23, '서울');


# 여러값 넣기
INSERT INTO classmates VALUES
	('홍길동', 23, '서울'),
	('홍길동', 24, '서울'),
	('홍길동', 26, '서울');
```



### select

![image-20220418063633913](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418063633913.png)

* LIMIT - OFFSET
* WHERE
* SELECT DISTINCT

``` sql
# 특정 필드 조회
SELECT rowid, name FROM classmates;

# 원하는 수만큼 데이터 조회
SELECT rowid, name FROM classmates LIMIT 1;

# 특정 부분에서 원하는 수만큼 데이터 조회 (3번째에 있는 하나만 조회)
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

# 주소가 서울인 경우
SELECT rowid, name FROM classmates WHERE address='서울';

# age값 전체를 중복없이 가져오기
SELECT DISTINCT age FROM classmates;

# 중복불가능한 값인 rowid 기준으로 삭제 (id가 5인 레코드 삭제)
DELETE FROM classmates WHERE rowid=5;


```



### SQLite는 기본적으로 id를 재사용한다

* 재사용 방지를 위해 `AUTOINCREMENT` 사용

``` sql
-- 테이블 생성
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
	);
```



### UPDATE (중복 불가능한 rowid 기준으로 수정)

``` sql
# classmates id가 5인 레코드 수정 , 이름 홍길동, 주소 제주도로 
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=5;
```

![image-20220418064528948](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418064528948.png)



* where 활용

``` sql
# user 테이블에서 age가 30이상인 모든 유저 컬럼 조회
SELECT * FROM users WHERE age >= 30;


#  user 테이블에서 age가 30이상인 유저 이름 조회
SELECT first_name FROM users WHERE age >= 30;

#  user 테이블에서 age가 30이상이고 성이 김인 사람의 나이와 성 조회
SELECT age, first_name FROM users WHERE age >= 30 AND last_name='김';
```



* aggregate functions (집계함수) : 값 집합에 대한 계산을 수행하고 단일 값을 반환
  * COUNT 
  * AVG, MAX. MIN, SUM - 기본적으로 integer일때 사용가능

``` sql
# 레코드 개수 조회
SELECT COUNT(*) FROM users;

# 30살이상 평균나이
SELECT AVG(30) FROM users WHERE age >= 30;

# 계좌잔액높은 사람, 그 액수 
SELECT name, MAX(balance) FROM users;

# 30살이상 평균계좌
SELECT AVG(balance) FROM users WHERE age >= 30;
```



* like (패턴일치)

![image-20220418065840022](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418065840022.png)

* like의 wildcards
  * % :  0개 이상의 문자
  * _ : 임의의 단일 문자
* like의 wildcards character
  * *
  * ?

``` sql
# 20인 사람
SELECT * FROM users WHERE age LIKE '2_';


# 지역번호 02
SELECT * FROM users WHERE phone LIKE '02-%';

# 준으로 끝나는 사람
SELECT * FROM users WHERE first_name LIKE '%준';

# 중간번호 5114
SELECT * FROM users WHERE phone LIKE '%-5114-%';
```



* order by
  * ASC : 오름차순 (기본)
  * DESC : 내림차순

``` sql
# 나이순으로 오름차순 정렬 상위10개 조회
SELECT * FROM users ORDER BY age LIMIT 10;

# 나이순,  성순으로 오름차순 정렬 상위10개 조회
SELECT * FROM users ORDER BY age, last_name LIMIT 10;


# 잔액으로 내림차순 정렬 상위10개 조회
SELECT last_name, fist_name FROM users ORDER BY balance DESC LIMIT 10;
```

* group by
  * where절 뒤에

``` sql
# 성에서 몇명있는지 조회
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

# 성에서 몇명있는지 조회
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

* alter table

``` sql 
ALTER TABLE 'table_name' RENAME COLUMN 'current_name' TO 'new_name';

# articles 테이블 명 news로 변경
ALTER TABLE  articles RENAME TO news;

# new 에 새 필드 추가
ALTER TABLE '테이블이름' ADD COLUMN '컬럼이름' '데이터타입설정';
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;

-- NOT NULL 설정 빼거나
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
```





# CRUD

## CREATE

``` sqlite
[1] CREATE 첫 번째 방법

>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>> aritcle. save()


[2] CREATE 두 번째 방법

>>> article = Article(title='second', content='django!!')
>>> aritcle. save()


[3] CREATE 세 번째 방법 (save필요없음)

>>> Article.objects.create(title='second', content='django!!')
```



* save()메서드
  * 객체를 DB에 저장함
  * save()하기 전에는 객체 ID 값을 알 수 없음
  * ID값은 Django가 아니라 DB에서 계산함
  * 단순히 모델을 인스턴스화하는 것은 DB에 영향을 미치지 않기 때문에 반드시 `save()가 필요`

* str 메서드

  ``` python
  def __str__(self):
      return self.title
  ```

  * 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음
  * 작성 후 반드시 shell_plus 재시작해야 반영됨

  ``` bash
  $ python manage.py shell_plus
  
  # shell_plus 이전에 설치사항
  $ pip install ipython
  $ pip install django-extensions 
  # settings.py에 등록 
  'django_extensions',
  ```



## READ

* QeurySet API method는 크게 2가지로 분류
  * 새 querysets 반환
  * querysets을 반환하지 않는다.

* 메소드

  * all()

  * get()

    * DoesNotExist 예외
    * MultipleObjectsReturned 예외

    ![image-20220418055016404](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418055016404.png)![image-20220418055127157](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418055127157.png)

  * filter()

  

``` sqlite
[1] all() - 현재 QuerySet의 복사본을 반환

>>> Article.objects.all()


[2] get() - 주어진 lookup 매개변수와 일치하는 객체 반환, pk같은 고유성 보장하는 조회에서 사용
* 객체 X - DoesNotExist 예외
* 둘 이상 객체 - MultipleObjectsReturned 예외

>>> Article.objects.get(pk=100)


[3] filter() - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

>>> Article.objects.filter(title='first')
```





## UPDATE

``` sqlite
[1] 
>>> article = Article.objects.get(pk=1)
>>> article.title = 'byebye'
>>> article.save()
```





## DELETE

``` sqlite
[1] 
>>> article = Article.objects.get(pk=1)
>>> article.delete()
```



## Field lookups

![image-20220418055718519](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418055718519.png)





# CRUD with views

``` python
def create(request):
    title  = request.GET.get('title')
    content  = request.GET.get('content')
    article = Aritcle(title=title, content=content)
    article.save()
    return render(request, 'article/create.html')

def index(request):
    1. DB로 받은 쿼리셋을 이후에 파이썬이 변경(파이썬 조작)
    articles = Aritcle.objects.all()[::-1]
    
    2. 처음부터 내림차순 쿼리셋으로 받음(DB가 조작)
    articles = Aritcle.objects.order_by('-pk')
```



<img src="C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060200568.png" alt="image-20220418060200568" style="zoom: 50%;" /><img src="C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060220633.png" alt="image-20220418060220633" style="zoom: 50%;" /><img src="C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060356391.png" alt="image-20220418060356391" style="zoom: 50%;" />

![image-20220418060434981](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060434981.png)

![image-20220418060446699](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060446699.png)

![image-20220418060500142](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060500142.png)





### variable routing

![image-20220418060645868](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060645868.png)

![image-20220418060636239](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060636239.png)





### edit

![image-20220418060837158](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060837158.png)

![image-20220418060831074](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220418060831074.png)



---



# Model Relationship 1

