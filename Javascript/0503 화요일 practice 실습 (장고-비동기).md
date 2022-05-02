## accounts/views.py follow함수

*  profile.html 보고 함



![image-20220503130810580](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220503130810580.png)



![image-20220503131134023](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220503131134023.png)

같은코드

![image-20220503131209945](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503131209945.png)



![image-20220503131336420](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503131336420.png)



## articles/views.py 

![image-20220503132100597](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503132100597.png)

data-article-id 는 웹페이지에서 데이터를 잠깐 담아두는 기능

![image-20220503131945161](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503131945161.png)

`mdn 데이터 속성 검색`

dom 구조에 데이터를 넣어두고 다른 조작을 하지않고 추가 정보를 스크립트로 접근할 수 있게 해줌



![image-20220503132319078](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503132319078.png)



![image-20220503132549694](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503132549694.png)

article에서 접근하면 like_users로 접근

다른 곳에서 접근하면 `타 테이블.like_articles`

![image-20220503132733461](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503132733461.png)





![image-20220503132821050](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503132821050.png)

네트워크를 보면 페이지가 다 바뀌고, 바뀌어서 

우리가 비동기식으로 처리해줘야함





## profile.html



![image-20220503133303330](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503133303330.png)

![image-20220503134004666](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503134004666.png)



![image-20220503134637410](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503134637410.png)



![image-20220503135212552](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135212552.png)

`mdn data-` 검색해보기

![image-20220503134916894](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503134916894.png)

`data-` 뒤에 필요한 것 넣어줌 



![image-20220503135123585](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135123585.png)



target은 이벤트를 발생시킨 노드가 들어옴



팔로우 누르고  -> target -> dataset -> ![image-20220503135353342](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135353342.png)있나 확인

![image-20220503135622811](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135622811.png)

![image-20220503135615637](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135615637.png)

![image-20220503135644020](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135644020.png)

![image-20220503135656211](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135656211.png)



![image-20220503135854124](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135854124.png)

새로 고침 후 저장하면

![image-20220503135845135](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503135845135.png)

에러가뜸

![image-20220503141602404](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503141602404.png)



## ACCOUNTS/ VIEWS



![image-20220503142030949](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503142030949-16515552311571.png)

![image-20220503142325475](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503142325475.png)

![image-20220503143210506](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503143210506.png)







![image-20220503142637265](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503142637265.png)

아이디 주기 follow-input

![image-20220503142836081](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503142836081.png)

![image-20220503143235928](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503143235928.png)





![image-20220503143406994](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503143406994.png)

변수명 follow-count주기

![image-20220503143613457](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503143613457.png)

세줄 추가

![image-20220503144010847](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503144010847.png)









----

## 비동기로 article 좋아요 처리하기

![image-20220503171942378](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503171942378.png)



![image-20220503171927772](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503171927772.png)

![image-20220503172117549](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503172117549.png)

위의 코드를 아래로 변경함



![image-20220503173214308](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173214308.png)





`data속성`

![image-20220503173313232](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173313232.png)

script 내에서 {{article.pk}} 같은 중괄호 두개로 접근불가능함

axios상에서 데이터를 넘길것이라 장고에서는 기존 방식으로 접근할 수 없기 때문에 

`data-*` 로 기존 dom구조에 데이터를 숨겨주는 것임

dom구조안에, 각각의 article.pk가 들어가는 것임



![image-20220503173624066](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173624066.png)

target의 dataset에 이렇게 적혀있을 것임![image-20220503173647144](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173647144.png)



----

![image-20220503173943809](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173943809.png)

여기까지하고 

좋아요를 눌러보면

![image-20220503173954089](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503173954089.png)

이 에러가 남 (에러나는 이유는 csrftoken을 안넘겨줬기때문에 당연히 남)







* csrftoken을 장고에서 가져오는 방법을 사용해야함 (django csrf token javascript)

![image-20220503174037127](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174037127.png)

![image-20220503174042768](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174042768.png)

![image-20220503174416588](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174416588.png)





아래를 적으면

![image-20220503174539535](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174539535.png)

![image-20220503174524356](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174524356.png)



html페이지가 전부다 다옴 하지만 내가 원하는건 이 리턴이 아니여서 뷰에가서 고칠거임



`뷰 like함수`

![image-20220503174652474](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174652474.png)

![image-20220503174732864](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174732864.png)







![image-20220503174847190](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174847190.png)

이렇게 바꾸어줌

![image-20220503174908437](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174908437.png)

![image-20220503174912318](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174912318.png)\

잘들어오고있음

![image-20220503174959383](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503174959383.png)





다시 인덱스로와서 

![image-20220503175238578](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503175238578.png)

조작





* 돔 조작하기

![image-20220503175256375](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503175256375.png)

like-{{article.pk}} 각각의 아이디를 달라지게하기



![image-20220503175645933](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503175645933.png)





* 좋아요 - 몇명이 좋아합니다 부분 ![image-20220503175802116](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503175802116.png)

![image-20220503175924334](0503 화요일 practice 실습 (장고-비동기).assets/image-20220503175924334.png)

53번째 줄을 64번째에 넣어주면됨



```html
{% extends 'base.html' %}

{% block content %}
  
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>작성자 : 
      <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      {% comment %} <form class="like-form" data-article-id="{{ article.pk }}"> {% endcomment %}
      {% comment %} <form action="{% url 'articles:likes' article.pk %}" method="POST"> {% endcomment %}
      
      <form class="like-form" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if user in article.like_users.all %}
          <button id="like-{{ article.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-{{ article.pk }}">좋아요</button>
        {% endif %}
      </form>
      <p>
        <span id="like-count-{{ article.pk }}">
          {{ article.like_users.all|length }}
        </span>
        명이 이 글을 좋아합니다.
      </p>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}

{% block script %}
  <script>
    // CODE HERE
    const forms = document.querySelectorAll('.like-form')

    forms.forEach( (form) => {
      // 기본 페이지에 요청
      // axios.get('http://127.0.0.1:8000/articles/')

      form.addEventListener('submit', (event) => {
        event.preventDefault()
        //console.log(event)
        const articleId = event.target.dataset.articleId
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
        //console.log(articleId)


        axios({
          method : 'post',
          url : `http://127.0.0.1:8000/articles/${articleId}/likes/`,
          headers : {'X-CSRFToken': csrftoken},
        }).then((res) => {
          //console.log(res)
          // 변수로 받아줌
          const count = res.data.likeCount
          const liked = res.data.isLiked // true or false
          const likeBtn = document.querySelector(`#like-${articleId}`)

          if(liked){
            likeBtn.innerText = '좋아요 취소'
          } else {
            likeBtn.innerText = '좋아요'
          }

          // 삼항연산자 -->  likeBtn.innerText = liked ? '좋아요 취소' : '좋아요'
          
          const likeCountElem = document.querySelector(`#like-count-${articleId}`)
          likeCountElem.innerText = count

        })
      })
    
    })
  </script>
{% endblock script %}

```

