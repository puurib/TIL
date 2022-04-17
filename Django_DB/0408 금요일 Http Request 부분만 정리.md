## 0408 금요일 Http Request

![image-20220416191803914](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416191803914.png)

* don touch me > django > markdown lectures
* ![image-20220416192032375](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416192032375.png) 얘는 modelform으로 만들어진 crud프로젝트 완성본
* ![image-20220416192108103](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416192108103.png) 얘가 ppt

---

* ![image-20220416192127934](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416192127934.png) 여기서 좀 더 마무리하는 것으로 수업 시작 (0406에서 이어지는 듯)

---



## http request

![image-20220416193827766](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416193827766.png)



### Django shortcuts functions

* 우리가 이미 사용하고 있던 render, redirect 함수가 있음

![image-20220416193931482](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416193931482.png)



![image-20220416194028517](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416194028517.png)

 

### get_object_or_404()

![image-20220416200951167](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416200951167.png)

* 원래 모델 manager인 objects에서 get()을 호출하지만, 
  해당 객체가 없을 경우 DoesNotExist예외(500에러) 대신 Http 404를 발생시킨다.
* get()에 경우 조건에 맞는 데이터가 없을 경우에 예외를 발생시킴
* 500을 받으면 어떤 상황인지 알 수 없는 에러임으로 `클라이언트 에러 page not found 404 `를 발생시켜준다.



> http 응답 상태 코드
>
> ![image-20220416194620985](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416194620985.png)
>
> 
>
> 100번 대 : 정보를 제공하는 응답
>
> 200번 대 : 성공적인 응답
>
> 300번 대 : 리다이렉트
>
> 400번 대 : 클라이언트 에러    ex) page not found 404 
>
> 500번 대: 서버 에러     



![image-20220416194939170](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416194939170.png)

 ![image-20220416200818321](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416200818321.png)





---

### get_object_or_404()를 사용해보자

![image-20220416201147701](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201147701.png)

이부분에서 에러가 발생함

![image-20220416201038761](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201038761.png)

![image-20220416201032535](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201032535.png)

500에러가 나왔지만 이 상황은, 클라이언트 리소스가 서버에 없는 경우(404 not found)임



`해결`

* django.shortcuts 에 get_object_or_404를 넣어주고

![image-20220416201213165](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201213165.png)

* article객체를 조회하는 것을 
  get_object_or_404 함수에 
  첫 번째 인자 : 모델, 
  두 번째 인자 : 조회 하고자 하는 키워드 인자

![image-20220416201318383](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201318383.png)

* 이렇게 하고 조회를 다시 해보면 404로 에러가 바뀜 (어떤 상황인지 인지하게 해줌)

![image-20220416201402117](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201402117.png)



---

### get_object_or_404()가 필요한 부분은 개별적으로 article을 조회하는 (pk사용) 부분임

![image-20220416201456432](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201456432.png)



### get_object_or_404(), get과의 차이점 

* 단일 객체를 조회하는 것은 같지만 예외가 발생했을 때 다르게 리턴해준다.



### 만약 get_object_or_404()를 쓰지않으면?

* http404를 넣어서 try, except 구문으로 만들어줌

![image-20220416201653154](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201653154.png)



### 전체 조회하는 부분을 

![image-20220416201903899](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416201903899.png)

* get_list_or_404는 필요하지 않음, 그 이유는 목록이 없을 경우에는 빈페이지를 받아도되니깐.
* get_list_or_404를 쓰는 경우에는 tmdb api로 영화 목록을 조회했을 때 영화 목록이 없는 경우에

![image-20220416202044380](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202044380.png)



---

 ## Django View decorators

![image-20220416202201190](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202201190.png)

* 데코레이터 함수의 인자로 원본 함수를 넣어서 기능만 추가해줌
* 이런 형태로 되어 있음 (예시)

![image-20220416202323147](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202323147.png)

---

### allowed http methods

![image-20220416202821792](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202821792.png)



 ![image-20220416202726284](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202726284.png)

* 삭제에 경우 get으로 보내면, redirect를 받는데 클라이언트 입장에서는 왜 받는지 모름
* 405 에러를 줌

![image-20220416202912128](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416202912128.png)

* 권장사항이 require_get 대신 require_safe쓰기 

![image-20220416203046405](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416203046405.png)





![image-20220416203118270](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416203118270.png)



* create, update가 필요함 

* 데코레이터를 사용하면 두가지만 들어가는거니, else는 GET일때만 됨
* 그리고 이 데코레이터에 허용되는 메소드가 아닐때는 405 에러를 발생시켜줌

![image-20220416203511353](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416203511353.png)





### 추가로 임포트해보기

![image-20220416203824783](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416203824783.png)

* index, detail에는 requre_safe(GET요청만 받는)

![image-20220416204125375](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204125375.png)

* delete는 requeire_POST가 필요함 (POST요청만 받는)

![image-20220416204201123](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204201123.png)

그런데, 여기서 생각해봐야할 것이 requeire_POST 데코레이터를 붙이면 수정이 필요해짐

POST인 경우에만 통과를 했을테니 55번줄을 볼필요가 없고, 58번줄처럼 아닐때를 염두할 필요가 없어짐

![image-20220416204234209](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204234209.png)

 

결국 이렇게 코드가 바뀜

![image-20220416204425351](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204425351.png)



---

### delete를 할 때 요청을 get으로 보내보자

![image-20220416204507038](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204507038.png)

![image-20220416204519494](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204519494.png)





### 그럼 여기서 request를 지우면 안되나요?

* 응 안돼, view함수가 동작하기 위한 필수 인자 

![image-20220416204559661](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416204559661.png)





### https://www.postman.com/

![image-20220416205708222](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416205708222.png)





get, post도 둘다 받을 수 있네~

![image-20220416205734160](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416205734160.png)

![image-20220416205807425](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416205807425.png)



![image-20220416205917559](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416205917559.png)





우리 메인 페이지로 보내면 403이 뜸

![image-20220416211059241](C:\Users\star3\AppData\Roaming\Typora\typora-user-images\image-20220416211059241.png)