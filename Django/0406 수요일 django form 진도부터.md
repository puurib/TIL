# 0406 수요일 django form 진도부터

>intro

![image-20220406205910434](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406205910434.png)

 

![image-20220406210109932](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406210109932.png)



## Form Class

![image-20220406210203164](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406210203164.png)





* python -m venv venv

* ctrl + shift + p 치고 select interpreter로 해서 venv선택

* 터미널 다시 키면

![image-20220406211427823](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406211427823.png)

이렇게 뜸



* $ pip install -r requirements.txt

* forms.py를 생성해서 작성해줌

![image-20220406210754948](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406210754948.png)

``` python
from django import forms

# Create your models here.
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```



* new.html 에  {{form}}으로 넣어주면 이렇게 뜸

![image-20220406211857652](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406211857652.png)



* as_p

![image-20220406212030519](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212030519.png)

![image-20220406212041804](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212041804.png)





* input의 타입이나 input은 대표적으로 form fields로 표현

![image-20220406212121865](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212121865.png)



* 둘째로 widgets으로 표현

![image-20220406212213272](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212213272.png)

![image-20220406212310215](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212310215.png)

* password일때

![image-20220406212434602](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212434602.png)

*  widget은 단순 표현만! 유효성 검사 처리는 form fields에서 처리

![image-20220406212522352](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212522352.png)



* 

![image-20220406212646074](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212646074.png)

choice는 튜플로 들어가야함

![image-20220406212951352](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406212951352.png)

![image-20220406213010328](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406213010328.png)



![image-20220406213024825](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406213024825.png)

왼쪽 값 =벨류, 오른쪽값 = 사용자에게 보이는 값





![image-20220406213111474](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406213111474.png)



django coding style을 쓰면



체크박스 멀티플

![image-20220406214918480](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406214918480.png)







## model form 

![image-20220406215102086](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406215102086.png)

![image-20220406220955862](0406%20%EC%88%98%EC%9A%94%EC%9D%BC%20django%20form%20%EC%A7%84%EB%8F%84%EB%B6%80%ED%84%B0.assets/image-20220406220955862.png)











---

# 오후





