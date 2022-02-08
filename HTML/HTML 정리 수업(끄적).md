# HTML 정리 수업(끄적)

## box model 속성 4가지 : content, padding, border, margin

* rgba에서 alpha는 투명도

  ![image-20220207124435468](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207124435468.png)



* 코드

![image-20220207124508275](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207124508275.png)

![image-20220207124825880](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207124825880.png)

* 높이, 너비 다 같은데 왜 패딩하나때문에 이렇게 나오냐고 ㅋㅋㅋ

![image-20220207124812566](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207124812566.png)



* 이러는 이유?  배경색은 padding까지 먹는다..

![image-20220207125026038](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207125026038.png)



## 박스 크기 같게 하기 : box-sizing

* 크기를 같게하는 법? box-sizing 을 이용해서 맞춰줄게! (기본은 content box였음)

  * 컨텐츠, 패딩, 보더까지 합쳐서 width와 height를 맞춰줌.. 길이 세어보면 동일함

  ![image-20220207125204103](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207125204103.png)

* 짠..

![image-20220207125128578](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207125128578.png)

---

## box 가운데 정렬하기 - margin: 0 auto (가로 auto 상하 0)

* 0 : 상하 좌우 다 0
* 0 auto : 상하 0 가로 auto
* 0 10 30: 위 좌우 아래
* 0 10 30 40: 시계방향

* 브라우저 창이 width보다 작아지면 스크롤바가 생김. --> 컨텐츠 보기엔 무리가 없지만 디자인 적으로 안좋다.
* 따라서 max-width를 줌 
  * 예를 들어서 max-width가 1200이라면, 작아지면 거기에 따라서 적용되고 1200보다 커지면 1200에 고정됨



## button - 인라인 요소의 수평 정렬? text-align

![image-20220207130022168](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207130022168.png)

![image-20220207130151674](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207130151674.png)

![image-20220207130140809](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207130140809.png)





## 수직 정렬이 어려움, 수직정렬 하는 법 : margin

* 위와 같이, 박스는 margin을 주고 인라인은 text-align을 주면됨
* 빨간 박스 05를 가운데로 내리고싶다.

![image-20220207131033769](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131033769.png)

### 방법 1: margin

* 마진을 줘봐 (크기 보고 나눠서 주기)

  ![image-20220207131153569](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131153569.png)

![image-20220207131146025](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131146025.png)



### 방법 2: position-relative (normal-flow를 기준으로 움직임;static)

* 포지션을 주면, top을 줄 수 있다.

![image-20220207131350143](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131350143.png)



### 방법 3: position-absolute (부모를 기준으로 움직임: not static) 많이 안씀..

* 



### 방법 4. line-hight (우리눈에는 안보이지만 높이를 부모높이만큼 맞춰버려서 수직정렬로 보이게 됨)

![image-20220207131837455](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131837455.png)

* line-hight는 절반값을 주면 됨.

![image-20220207131821270](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207131821270.png)



### 방법 5. line-hight (인라인)



### 시험 선택자 잘나옴..

![image-20220207132020348](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207132020348.png)

---

---

## emmit

> - `>`  태그를 만들고 들여쓰기
> - `*n` 반복
> - `+` 줄바꿈 + 다음 태그 추가
> - `.` class 지정
> - `#` id 지정
> - `{content}` 내용 입력

* 이렇게 치고 tab 누르면 테이블 뚝딱

![image-20220207132300182](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207132300182.png)

* `div*5.box`

![image-20220207132400934](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207132400934.png)

* `어떤 태그 > 다른 태그` : 어떤 태그를 만들고 그 태그 안쪽에 다른 태그를 만들겠다.
* `어떤 태그 * 5` : 어떤 태그를 5개 만들겠다.
* `+` : 형제 요소를 만들어 줌

* `태그.클래스명` : 클래스명으로 클래스가 만들어짐
* `태그#아이디명` : 아이디명으로 아이디가 만들어짐

* `{컨텐츠}` : 태그의 컨텐츠를 채워줌

![image-20220207132749870](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220207132749870.png)

---

---

## css 선택자 게임 사이트

https://flukeout.github.io/

---

# 이 밑에 다 시험.. 

### Float : 블록요소 인라인요소를 감쌀 때 사용(뉴스 레이아웃)

normal flow를 벗어난다. normal flow는 왼쪽 상단, 위쪽으로 모든 요소가 붙으려는 성격이 있는데 이러한 걸 따르는 것.- 시험!!!!

* left 속성 :

* right 속성 :

#### float 실습 코드

* `lorem숫자` : 숫자에 맞는 임의의 숫자가 생성.
* 사각형 옆에는 마진이 있음.

![image-20220208092251154](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208092251154.png)

* css를 다 주고, 개발자 도구 안주고 코드만 보고 마진, 패딩 계산하는 시험 문제 나옴 시험
* p태그를 없애면 겹쳐짐.

![image-20220208092607777](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208092607777.png)

* 이래서 float clearing --> clearfix가 나옴.



### float clearing --> clearfix (요즘은 flex를 쓴다.)

* clear가 적용하는 애부터 float로 인한 정렬 요소를 없앴다.
* 원래라면 초록 뒤에 파랑인데, 정렬요소가 없어짐..

![image-20220208093205848](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208093205848.png)

* p 태그를 넣어줬는데 clear: right를 쓰지 않는 이유가 이 코드에서는 left만 있기 때문.

  그래서 clear: both;

* 

![image-20220208093427594](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208093427594.png)



### 의사요소 생성자 = 가상요소 생성자 ::

* content를 만든 다음, 가상요소를 만드는데, 내용은없고 display는 블럭요소 clear를 먹인 가상요소를 사용하겠다.

![image-20220208093859889](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208093859889.png)

![image-20220208093839199](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208093839199.png)



## float 실습

![image-20220208094131853](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208094131853.png)

조심!!!! 

인라인요소 정렬!

text-align: center;

line-height 

![image-20220208100656451](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208100656451.png)

![image-20220208100739628](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208100739628.png)

```
# float를 flex로 적용한다면?
.container {display: flex}
```



![image-20220208101851881](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208101851881.png)



### flexbox - flex container , flex item (수평이 될 요소들을 컨테이너로 묶는 것) 왜냐, 수직정렬은 괜찮은데 수평정렬이 어렵기 때문에.

어려운 이유는 container에 적용되는 속성, item에 적용되는 속성이 다름..

* container : display, flex-flow, justify-content
* item : order, flex, 

![image-20220208101302363](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208101302363.png)

![image-20220208101703509](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208101703509.png)



### container에 적용되는 속성들

```
- `display` - Flex Container를 정의
- `flex-flow` - `flex-direction` 과 `flex-wrap` 을 줄여서 쓸 수 있음
- `flex-direction` - item들의 주 축(main-axis) 설정
- `flex-wrap` - item들의 줄 바꿈 설정
- `justify-content` - 주 축(main-axis)의 정렬  방법 설정
- `align-content` - 교차 축(cross-axis)의 정렬 방법 설정 (2줄 이상)
- `align-items` - 교차 축(cross-axis)의 정렬 방법 설정 (1줄)
```



![image-20220208102031755](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208102031755.png)



#### `display`  에는 flex, flex-inline 두개 들어갈 수 있음

flex를 하면 컨테이너가 수직정렬로 쌓이고 	flex-inline으로 하면 수평으로 컨테이너가 쌓임

![image-20220208101942248](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208101942248.png)



#### `flex-direction` - item들의 주 축(main-axis) 설정

각각의 축을 가지고 있다. 

아이템들을 어떻게 정렬할 것인지? 메인축을 어디로 잡을 것인지 ???

* flex-direction의 속성값 = 4가지(row, row-reverse, column, column-reverse)

어디로 쌓이는지~~ 

![image-20220208102443773](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208102443773.png)

reverse (별로 안씀)

![image-20220208102659184](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208102659184.png)

#### flex-wrap : item들의 줄 바꿈 설정 (nowrap, wrap, wrap-reverse )

* nowrap: 한줄로 모든 아이템을 표시하겠다. 디폴트값

  화면을 줄여도 모든 아이템을 한줄로 보여줌 크기에 따라 아이템이 줄어든다.

![image-20220208102928523](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208102928523.png)

![image-20220208102939042](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208102939042.png)

* wrap: viewport 크기에 따라서 아이템이 여러줄로 보인다.

```
display : flex;
flex-wrap: wrap;
```



![image-20220208103034867](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208103034867.png)

* wrap-reverse: 10은 위에 있고 나머지가 내려감.. 더 줄이면 9가 올라감..





#### flex-flow` - `flex-direction` 과 `flex-wrap` 을 줄여서 쓸 수 있음

flex-flow : `flex-direction` 한 칸 띄고 `flex-wrap`



#### justify-content(flex에서 제일 중요 별표)

![image-20220208103445134](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208103445134.png)

```
flex-start : flex-direction에 따라 당연히바뀔 수 있음
flex-end : flex-direction에 따라 당연히바뀔 수 있음
flex-center : 주축을 기준으로 함. (main)
space-between (유튜브라이브 때 열심히 대답했다고함..)
space-around (유튜브라이브 때 열심히 대답했다고함..)
space-evenly
```



* space-between 나머지 여백 1/n

아이템 사이의 간격이 다 똑같게 정렬해줌 (시작, 끝을 끝에 붙이고 나머지 여백은 균등)

![image-20220208104514160](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208104514160.png)

![image-20220208104535716](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208104535716.png)



![image-20220208103935969](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208103935969.png)

* space-around: 각각의 아이템의 여백이 같을 것인지?

![image-20220208104217329](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208104217329.png)

* space-evenly : 모든 여백을 균등하게



#### align-content, align-items

![image-20220208104719058](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208104719058.png)



#### align-content

* flex-wrap이 nowrap이면 align-content를 주는 의미가 없어짐. (상충됨.)
  * flex-wrap은 모든 아이템을 1줄로 만들고 싶어하는데 align-content은 2줄이상일 때 사용하니깐

* stretch : 아이템을 꽉꽉 늘림.. (align-content의 기본값)

  flex-start

  flex-end

  center(교차축을 기준으로 함)

  space-between

  space-around

![image-20220208105601983](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208105601983.png)

실습해보기





#### align-items

align-contents랑 똑같은데 

baseline이라는 것만 추가됨. : 문자 기준선에 맞춰서

![img](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/unknown.png)

![image-20220208105940096](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208105940096.png)



#### grow는 증가율, shrink는 감소율 basis는 기본너비라고 알고 있으면됨 shrink는 시험안나옴 (flex-grow 시험 나옴)

* Flex Item을 위한 속성들
  - `order` - Item의 순서를 설정
  - `flex` - `flex-grow` , `flex-shrink` , `flex-basis` 에 대한 단축 속성!
  - `flex-grow` - Item의 너비 증가(grow) 비율 설정 (뷰포트를 늘일때 아이템이 늘어나는 너비 증가율)
  - `flex-shrink` - Item의 너비 감소(shrink) 비율 설정 (뷰포트를 늘일때 아이템이 늘어나는 너비 감소율)
  - `flex-basis` - Item의 기본 너비 설정 기본값은 auto(알아서 정해주세요.)가 기본값
    (와!!! 이게 ... 신기하네 inline에도 줄수있음, 그러나안알아도됨)
  - align-self : 교차축을 기준으로 item을 정렬하는 방법을 설정해요 기본값은 auto





* order : 아이템 중에 1번을 맨뒤로 보내고 싶은데?!
  * order에 5를 적었다고 5로 안감.............?! 맨뒤로감..................모르겠는데!

![image-20220208111005745](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208111005745.png)

![image-20220208110949126](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208110949126.png)

![image-20220208110347907](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208110347907.png)



* flex : 1 `어떤값` `생략`

  `생략`하면 `생략`에 0이 들어감.. (auto가 아니고) - 시험에는 안나옴



#### flex-grow : item의 너비 증가의 비율 설정 (시험)

증가, 감소를 아무리 줘도 flex-container가 nowrap이 아니면 의미가 없음

wrap이면 줄이 바뀌어서 내려가니까 동작을 안하니깐...!!!!!!!!!!!!!!



줄어드는 비율이 다르게 때문에 가운데가 더 넓지만 줄일 수 있다..ㅁ

![image-20220208111815082](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208111815082.png)

![image-20220208111755638](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208111755638.png)



#### flex-shrink 

a랑 b랑 박스 크기가 100px로 같고 90px로 뷰포트를 줄였을때 a는 1, b는 2라면, a는 30px b는 60px

![image-20220208112200642](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208112200642.png)

![image-20220208112335042](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208112335042.png)

![image-20220208112304304](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208112304304.png)



* 문제는 a,b가 크기가 다를때임 (둘다 45px씩 줄어들음..)

![image-20220208112546904](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208112546904.png)



#### 세로 정렬 가로 정렬 justify-content: center; align-items: center; 

![image-20220208124910820](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208124910820.png)



align-content: center는 왜 안될까? : 두줄이상일 때 효과를 발휘함.

![image-20220208124919453](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208124919453.png)



## 부트스트랩

1.  다운로드 받아서 넣어주기
2. cdn으로 넣어주기 : 바디 닫는 태그 위에 , dom 모델로 



### rem = 루트 em (1이 16px이구나!)

![image-20220208130143673](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208130143673.png)



![image-20220208130313224](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208130313224.png)



### grid

* 기본요소 : container, row, column 이 있다.

  * 컨테이너는 부트스트랩의 가장 기본적인 레이아웃요소

  * 컨테이너는 가로 중앙에 기본으로 배치해줌

  * 클래스이름

    ![image-20220208130946226](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208130946226.png)

    * container : 안에 있는 애들이 반응형이 됨.
    * container-fluid : width를 100%로 지정하는 거구나.
    * container-{breakingpoints} : 크게 중요하진 않음.. 이런것도 있다. 



![image-20220208131634244](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208131634244.png)



* 12개의 column, 6개의 breakingpoints가 있음
* container를 만들고 row를 만들고 column을 배치 정렬
* `col-A-B` A에는 grid option의 breakingpoints가 들어감
* row는 아무런 것을 적지않으면  block요소로 한줄을 차지
* 

![image-20220208130736355](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208130736355.png)

* 





## rem, em 차이 

![image-20220208153043228](HTML%20%EC%A0%95%EB%A6%AC%20%EC%88%98%EC%97%85(%EB%81%84%EC%A0%81).assets/image-20220208153043228.png)

## vscode



ctrl alt 방향키

커서 놓고 alt + 방향키

