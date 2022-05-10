# vue01 - vue cdn

* FE Development
* SPA



## CDN 과 CLI

![image-20220515201617757](vue정리.assets/image-20220515201617757.png)



* el은 기본 속성



* 바인딩 <span v-bind:title="message">
* 조건문 v-if

![image-20220515201918603](vue정리.assets/image-20220515201918603.png)

* 반복문 v-for

![image-20220515202030803](vue정리.assets/image-20220515202030803.png)

* 사용자 입력 핸들링

인풋값넣기, 엔터, 버튼클릭, 등등

![image-20220515202146947](vue정리.assets/image-20220515202146947.png)

* v-model 사용자 입력 핸들링

![image-20220515202315508](vue정리.assets/image-20220515202315508.png)

쌍방향으로 바뀜

---

![image-20220515202426128](vue정리.assets/image-20220515202426128.png)

![image-20220515202504458](vue정리.assets/image-20220515202504458.png)

![image-20220515202554321](vue정리.assets/image-20220515202554321.png)

this는 뷰 인스턴스가 아님!

data, method정의 화살표함수 X

---

![image-20220515202817581](vue정리.assets/image-20220515202817581.png)

---

![image-20220515203016720](vue정리.assets/image-20220515203016720.png)

![image-20220515203130274](vue정리.assets/image-20220515203130274.png)



v-bind 는 :

v-on:click은 @click

![image-20220515203346008](vue정리.assets/image-20220515203346008.png)



* v-show 

if문을 쓰면 돔에서 사라짐

v-show는 돔에는 남아있는데 안보이는거뿐

![image-20220515203439695](vue정리.assets/image-20220515203439695.png)

![image-20220515203531183](vue정리.assets/image-20220515203531183.png)



![image-20220515203838674](vue정리.assets/image-20220515203838674.png)

key값이 없어도 되는데 권장

dix, id 등

---

![image-20220515203941738](vue정리.assets/image-20220515203941738.png)

![image-20220515204415755](vue정리.assets/image-20220515204415755.png)

:class=artive

![image-20220515204626443](vue정리.assets/image-20220515204626443.png)

![image-20220515204708377](vue정리.assets/image-20220515204708377.png)

함수 선언안해줘도 알아서 양방향 통신이 된다



![image-20220515204741025](vue정리.assets/image-20220515204741025.png)

data : 정적인 놈

computed : 동적인 놈

---

![image-20220515205014506](vue정리.assets/image-20220515205014506.png)

![image-20220515205118042](vue정리.assets/image-20220515205118042.png)



---

![image-20220515205221726](vue정리.assets/image-20220515205221726.png)

----

![image-20220515205546837](vue정리.assets/image-20220515205546837.png)

created -> mounted -> S

![image-20220515205602683](vue정리.assets/image-20220515205602683.png)



## vue02 - vue cli

![image-20220515205849931](vue정리.assets/image-20220515205849931.png)

![image-20220515210151017](vue정리.assets/image-20220515210151017.png)

![](vue정리.assets/image-20220515210426415.png)

이거 ~/ㅇㅇㅇ/ 뷰이름 이 가능해짐

![image-20220515210523759](vue정리.assets/image-20220515210523759.png)

![image-20220515210626631](vue정리.assets/image-20220515210626631.png)



![image-20220515210859553](vue정리.assets/image-20220515210859553.png)

![image-20220515210914722](vue정리.assets/image-20220515210914722.png)



assets 사진 로고 등

app.vue가 보여주는 것

![image-20220515211120323](vue정리.assets/image-20220515211120323.png)







![image-20220515211336736](vue정리.assets/image-20220515211336736.png)

about컴포넌트한테 줄거(자식)



parent-data라는 이름으로 parentDate value

자식 props에 지정

![image-20220515211457211](vue정리.assets/image-20220515211457211.png)

![image-20220515211516583](vue정리.assets/image-20220515211516583.png)

cli는 함수, cdn은 함수 안해도 됨

![image-20220515211708258](vue정리.assets/image-20220515211708258.png)

실수!!!!

숫자 전달하려면 바인딩, 문자는 그냥 !



![image-20220515211741675](vue정리.assets/image-20220515211741675.png)

이걸 안하려고 쓰는게 vuex다..ㅎ



![image-20220515211910877](vue정리.assets/image-20220515211910877.png)

![image-20220515212007644](vue정리.assets/image-20220515212007644.png)



![image-20220515212101987](vue정리.assets/image-20220515212101987.png)

---

###  vue router 

![image-20220515212257304](vue정리.assets/image-20220515212257304.png)

![image-20220515212414939](vue정리.assets/image-20220515212414939.png)



클릭이벤트를 차단하여 브라우저가 새로고침을 안함

a 태그임 

![image-20220515212437504](vue정리.assets/image-20220515212437504.png)

그냥 넘어가는 거처럼 보임

![image-20220515213406434](vue정리.assets/image-20220515213406434.png)





## vuex

![image-20220515213832323](vue정리.assets/image-20220515213832323.png)



![image-20220515213653893](vue정리.assets/image-20220515213653893.png)

state에 싹다 정리~



3/ this.$store.commit

4/ this.$store.dispatch

mapstate

![image-20220515214706622](vue정리.assets/image-20220515214706622.png)

![image-20220515214904135](vue정리.assets/image-20220515214904135.png)

![image-20220515215207617](vue정리.assets/image-20220515215207617.png)







![image-20220515215921941](vue정리.assets/image-20220515215921941.png)

todo값을 내려줌 props로 

![image-20220515220345355](vue정리.assets/image-20220515220345355.png)

구조분해할당으로





state -> actions -> mutions -> getter

![image-20220515220605645](vue정리.assets/image-20220515220605645.png)





