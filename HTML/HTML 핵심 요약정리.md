# HTML 핵심 요약정리 (시험 대비용)

## 1. 현재의 웹 표준은 WHATWG 이다.

* W3C와 WHATWG가 웹 표준을 놓고 경쟁을 벌이다 기술 표준화 싸움에서 WHATWG가 승리함.





## 2. 모르는 용어 검색 : `mdn + 모르는 용어` (모질라), w3shcool에서 대부분 찾을 수 있다.

* can i use? 에서 `semantic elements`를 찾아볼 수 있다.





## 3. HTML에 필요한 VScode 확장과 환경설정(css표준 spacebar 2칸 등)을 했다.





## 4. 크롬 개발자 도구 

## F12 = contrl + shift + l(엘) = 도구 더보기 > 개발자 도구

* 여기서 알아야 할 것은, 크롬에서 개발과 관련된 다양한 기능을 제공한다는 것
* chrome devtools

![image-20220204132357812](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204132357812.png)





## 5. HTML의 정의 : 한 마디로 웹페이지를 구조화하기 위한 언어

* 하이퍼링크(참조)를 통해 한 문서에서 다른 문서로 즉시 접근할 수 있다.
* 과거에는 선으로 이어지듯 기존의 선형적인(줄 선, 형태 형) 텍스트가 아닌 비선형적으로 이루어진 텍스트를 의미하며 인터넷의 등장과 함께 대두되었다.
* ''구글효과''라는 말도 생길만큼 인간의 기억 방식을 바꿈

* 뜻은 hyper(초월하다) text markup language :  텍스트를 초월해서 다른 곳으로 뛰어넘을 수 있는, 태그와 데이터로 문서의 구조가 표현된 언어

![image-20220204132752367](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204132752367.png)





## 6. HTML 기본 구조

* html : 문서의 최상위(root) 요소
* head : 문서 메타데이터 요소 : 일반적으론 브라우저에는 보이지 않아요.....!
* body : 문서 본문 요소

![image-20220204132935842](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204132935842.png)

![image-20220204132953074](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204132953074.png)





## 7. Open Graph Protocol

* Open Graph Protocl : 이게 왜 있나 했는데, 메타 데이터를 그냥 작성하면 알아보기 힘드니까, 제목이나 설명 등을 쓸 수 있도록 정의하는 것 같다. 

![image-20220204133019865](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204133019865.png)





## 8. DOM(Document Object Model) 트리

* 랜더링 --> 2차원을 3차원으로 만드는 것

**![image-20220204133114982](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204133114982.png)**





## 9. HTML 문법 (요소, 속성, 시멘틱 태그)

### 1. 요소(element) : 시험) 내용이 없는 태그들 주의해서 보기

![image-20220204133249916](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204133249916.png)

![image-20220204133308231](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204133308231.png)

* html은 오류를 반환하지 않고, 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 힘들어질 수 있다. 여/닫 태그쌍이 있다면 잘 확인하자.





### 2. 속성(attribute)

![image-20220204134000256](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134000256.png)

![image-20220204134021188](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134021188.png)

![image-20220204134050077](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134050077.png)

![image-20220204134137563](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134137563.png)

![image-20220204134213751](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134213751.png)





### 3. 시맨틱 태그 for 검색엔진 최적화(SEO) : 의미론적 요소 (시험: 개념 객관식)

![image-20220204134337647](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134337647.png)

![image-20220204134424689](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134424689.png)

![image-20220204134510311](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134510311.png)





### 4. HTML with 개발자 도구

![image-20220204134625337](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134625337.png)

![image-20220204134854861](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134854861.png)







## 10. HTML 문서 구조화

### 1. 인라인 `<span> </span>`/ 블록 요소 `<div> </div>`

![image-20220204135014783](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204135014783.png)

![image-20220204135038337](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204135038337.png)



### 2. 텍스트 요소

![image-20220204135341084](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204135341084.png)







---

# HTML 실습 코드

## 1번 코드 : 

![image-20220204134255408](HTML%20%ED%95%B5%EC%8B%AC%20%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC.assets/image-20220204134255408.png)