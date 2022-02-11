# PJT 1회차 (Python을 활용한 데이터 수집)

## 향후 관통 프로젝트 구성 (매주 금요일 총 10회 예정)

### 관통프로젝트

* 한 주간 배운 내용을 바탕으로 명세서 기반의 프로젝트

* 목표 : 페어 프로그램, Git을 활용한 협업 등을 통해 단계적 협업 능력 향상





### 명세서 구조

* 준비사항 : 개발 언어/프로그램, 라이브러리, 외부 데이터 등
* 요구사항 : 제시된 요구사항에 맞춰 개발 진행
* 결과 : 반드시 결과로 나타난 폴더 구조를 참고하여 작성 (제출해야한다니.......)





## git

### git 이란? = 분산 버전 관리 시스템

`PPT 만들 때, 진짜진짜 최종, 최종, 이게정말 최종` 처럼 만들어 본 적이 있는데..

세상 사는 것 다 똑같다?

다른 사람들도 이런 고민을 했고 파일을 따로 만드는 것이 아닌, 

버전으로 관리할 수 있게 도와주는 프로그램이 git이다. (버전 관리에서 비슷한 느낌은 `구글 docs`가 있다.)



* 분산 버전 관리 시스템 (DVCS, Distributed Version Control System)
* 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
* 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율





### CVCS vs DVCS

* 중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용 (---> 파일을 다운받아서 변경 후 버전을 고쳐서 올려야 했다..귀찮아!)
* 분산버전관리시스템은 원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유





### CLI vs GUI

* 인터페이스 (Inter + Face) : 얼굴을 맞대는 접점
* CLI : 명령 기반의 인터페이스
* GUI : 그래픽 인터페이스





### git 명령어

``` bash
$ git log  # 고유한 해시값이 생성된다 (버전 확인)
```

![image-20220121100357792](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121100357792.png)

``` bash
$ git status  # 변경된 사항들을 알려준다 (상태 확인)

$ ls -a 하면 # ./ ../ 도 보임

$ pwd # print working directory 현재 작업 폴더 출력

$ rm `파일`  #remove = rm

$ rm -r `디렉토리`  # 재귀적으로 지우겠다. 이 폴더 내부의 폴더도 지우고 다 지우겠다~~

$ touch `파일`

$ mkdir `디렉토리`
```



### git 명령어

``` bash
$ git init  # git 저장소 초기화 후 .git이 생김
```

* `.git` 에 손대면 안됨

* `.git`으로 버전관리가 시작됨





### 로컬에서의 git 기초 흐름

![image-20220121103731974](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121103731974.png)

![image-20220121103920861](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121103920861.png)



1. 작업을 하고
2. 변경된 파일을 모아 (add) ---> Staging Area로 올림
3. 버전으로 기록한다. (commit) ---> Repository로 올림





### git의 작업 공간

1. Working Directory : 작업 중인 실제 디렉토리
2. Staging Area : 버전으로 기록하기 위한 파일 변경 사항의 목록 
3. Repository : 커밋(버전)들이 기록되는 곳





### 원격저장소의 git 기본 흐름

``` bash
$ git clone : 로컬 저장소가 없는 경우 원격 저장소를 복제 

$ git pull : 로컬 저장소, 원격 저장소 둘 다 있는 경우 

$ git pull origin master 

$ git push 

$ git remote add origin `깃 저장소`

$ git remote -v : 상세 보기
```

![image-20220121105231788](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121105231788.png)

* `Shift` + `Insert` : 붙여넣기

``` bash
$ git log --oneline

$ 
```

![image-20220121110210378](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110210378.png)

![image-20220121110305020](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110305020.png)

![image-20220121110221175](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110221175.png)





### 프로젝트 

![image-20220121110613569](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110613569.png)

![image-20220121110637115](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110637115.png)

![image-20220121105514318](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121105514318.png)

### 프로젝트 제출 가이드

![image-20220121112058044](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112058044.png)

readme.md에 프로젝트에서 뭘 배웠는지, 오류사항, 추가학습한 것

![image-20220121112253377](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112253377.png)





###  파일 입력

![image-20220121110745868](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110745868.png)

![image-20220121110931757](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121110931757.png)





### JSON (JavaScript Object Notation)

![image-20220121111033239](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111033239.png)

![image-20220121111539025](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111539025.png)





### Pprint (예쁘게 출력~)

![image-20220121111556798](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111556798.png)





### 리스트 순회 - 딕셔너리의 key로 접근

![image-20220121111704835](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111704835.png)

![image-20220121111900713](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111900713.png)

* 근데 키가 없어..............



### 딕셔너리 접근 방법 (dict.get(key, default))

![image-20220121111918689](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121111918689.png)

![image-20220121112012791](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112012791.png)

* 에러가 나도됨~ 때에 따라 사용하는게 다름!





### problem.py

![image-20220121112342982](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112342982.png)

![image-20220121112438721](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112438721.png)



* 제목만 출력

![image-20220121112558554](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112558554.png)

* 다른 형태로 출력하고 싶다면? 

![image-20220121112646611](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121112646611.png)





* 아이콘 바꾸기><

![image-20220121130855437](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121130855437.png)

![image-20220121151333342](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121151333342.png)

![image-20220121151601353](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121151601353.png)

![image-20220121151650313](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121151650313.png)

![image-20220121151852273](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121151852273.png)





C



![image-20220121154716359](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121154716359.png)



![image-20220121154828145](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121154828145.png)

![image-20220121172519174](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121172519174.png)



함수 다 써도됨

max 도



리스트 개수 : len()함수



4번 문제

제이슨에서 읽어서 반환해서 새로운 딕셔너리 만드는 것





5번 

문자열의 길이를 테스트 

빈값이 입력되면 len이 0

![image-20220121172936932](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121172936932.png)

len(str) == 0 이면

하나라도  A or B

if 아이디 and 비밀번호 :

​		return False

둘다 



6번

인덱스 [-1]

"9" , 9

숫자를 문자로 만들어서 비교해주기





회문

``` python
def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True
```

![image-20220121175814637](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121175814637.png)

![image-20220121175935065](PJT%201%ED%9A%8C%EC%B0%A8%20(Python%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91).assets/image-20220121175935065.png)



``` python
def is_pal_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])   
    else:
        return False
```



