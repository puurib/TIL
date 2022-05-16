

![image-20220517095250338](0517 화요일 vue api 서버 활용 - serializers 부분만.assets/image-20220517095250338.png)



### serializers

* articleSerializer는 profileSerializer에서만 사용해서 안에서 정의하고 사용
* articles, like_articles는 둘다 복수의 사람이 한번에 쓸 수 있으니 many=True

![image-20220517095004697](0517 화요일 vue api 서버 활용 - serializers 부분만.assets/image-20220517095004697.png)



![image-20220517111927348](0517 화요일 vue api 서버 활용 - serializers 부분만.assets/image-20220517111927348.png)



---

![image-20220517101031557](0517 화요일 vue api 서버 활용 - serializers 부분만.assets/image-20220517101031557.png)

시리얼라이저가 길어질때는 폴더를 만들고, 모델별로 py를 만든다.

![image-20220517101258576](0517 화요일 vue api 서버 활용 - serializers 부분만.assets/image-20220517101258576.png)