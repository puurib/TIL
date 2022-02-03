# HTML

## 0. 시험

1. 시맨틱 요소

2. colspan, rowspan



## 1. 현재의 웹 표준 : WHATWG

* W3C와의 기술 표준화 주도권 싸움에서 WHATWG가 승리했다. (웹 표준이 하나로 합쳐짐)
* 크롬이 브라우저다.

![image-20220203092402163](C:%5CUsers%5Cstar3%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220203092402163.png)



![image-20220203092454822](HTML.assets/image-20220203092454822.png)



## 2. 유용한 사이트 모음 (이 두 사이트에서 대부분을 알 수 있을 것)

* `html`에서 궁금한게 생기면 `mdn` 앞에 붙이기 ex) `mdn 모르는용어` -- 모질라 
  * https://developer.mozilla.org/ko/docs/Web/HTML
* w3shcool
  * https://www.w3schools.com/html/



## 3. VScode 확장+ 환경 설정

1. open in browser 설치

![image-20220203093241882](HTML.assets/image-20220203093241882.png)

* alt+b를 하면 바로 브라우저로 열림



2. auto rename tag 설치

![image-20220203093613360](HTML.assets/image-20220203093613360.png)

3. highlight matching tag 설치

![image-20220203093750527](HTML.assets/image-20220203093750527.png)



4. 환경 설정 (html의 경우 space 2칸이 마크업 스타일 가이드..)

* 컨트롤+,(콤마)로 설정 --> settings.json에서 편집 --> 아래 코드를 settings.json의 맨아래 `}` 위에 붙여 넣기

![image-20220203094054722](HTML.assets/image-20220203094054722.png)

``` 
	"editor.tabSize": 2,
    "[python]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "python.languageServer": "Pylance",
    "python.analysis.extraPaths": [
        "./sources"
    ],
    "workbench.startupEditor": "none",
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook"
    },
    "notebook.cellToolbarLocation": {
        "default": "right",
        "jupyter-notebook": "left"
    },

	"terminal.integrated.defaultProfile.windows": "Git Bash",
    "explorer.confirmDelete": false,
    "editor.renderWhitespace": "all",
    "editor.fontFamily": "D2coding, Consolas, 'Courier New', monospace",
    "liveServer.settings.donotShowInfoMsg": true,
    "files.associations": {
        "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "window.zoomLevel": 1,
    "security.workspace.trust.untrustedFiles": "open",
    "diffEditor.renderSideBySide": false,
    "extensions.ignoreRecommendations": true,
    "workbench.iconTheme": "material-icon-theme",
    "explorer.confirmDragAndDrop": false,
	"terminal.integrated.defaultProfile.windows": "Git Bash",
    "explorer.confirmDelete": false,
    "editor.renderWhitespace": "all",
    "editor.fontFamily": "D2coding, Consolas, 'Courier New', monospace",
    "liveServer.settings.donotShowInfoMsg": true,
    "files.associations": {
        "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "window.zoomLevel": 1,
    "security.workspace.trust.untrustedFiles": "open",
    "diffEditor.renderSideBySide": false,
    "extensions.ignoreRecommendations": true,
    "workbench.iconTheme": "material-icon-theme",
    "explorer.confirmDragAndDrop": false,
```



5. 윈도우 - 기본앱 크롬으로 

![image-20220203095100933](HTML.assets/image-20220203095100933.png)





## 4. 개발자 도구 = F12 = Ctrl+shift+l(엘)

![image-20220203094811245](HTML.assets/image-20220203094811245.png)





## 5. HTML이란?

![image-20220203100452443](HTML.assets/image-20220203100452443.png)

* hyper : 초월하다, 뛰어넘다

  * hyperlink : 한 페이지에서 다른 곳으로 이동,
  * hypertext : 그냥 텍스트가 아니라, 다른 곳으로 뛰어 넘을 수 있다.
    *  hyperlink를 통해서 이동한다.

* markup : 마크로 둘러싸인 언어 (태그로 데이터와 문서의 구조를 표현)

* markup 언어 : 태그와 데이터로 문서의 구조를 표현하는 것

* markdown : 마크업을 이용해서 만들어졌다.

  * up, down의 의미는 x
  * 개발자의 연필이다.
  * 문서 작성시에 구조와 내용을 함께 적기위해 만들어진 마크업 언어

  ![image-20220203101422407](HTML.assets/image-20220203101422407.png)

  

  ![image-20220203100342353](HTML.assets/image-20220203100342353.png)





## 6. HTML 기본 구조

![image-20220203101628657](HTML.assets/image-20220203101628657.png)

![image-20220203102139930](HTML.assets/image-20220203102139930.png)

![image-20220203102307171](HTML.assets/image-20220203102307171.png)



## 7. DOM 트리 (계층 구조)

![image-20220203102854894](HTML.assets/image-20220203102854894.png)

* 랜더링 --> 2차원을 3차원으로 만드는 것

## 1. 요소는 태그, 내용으로 구성

* 소문자로 쓰기!!!!!!주의

![image-20220203103453296](HTML.assets/image-20220203103453296.png)

### 2. 내용이 없는 태그

* `<br>`: 개행
  * `<br/>` : 구버전 개행
* 

![image-20220203103749795](HTML.assets/image-20220203103749795.png)

### 3. 속성 

* 여는 태그 한칸 띄고, 속성을 써줌.
* 속성값은 문자

![image-20220203104028420](HTML.assets/image-20220203104028420.png)

![image-20220203104121703](HTML.assets/image-20220203104121703.png)

![image-20220203104335832](HTML.assets/image-20220203104335832.png)

* 태그와 상관없이 사용가능한 속성 - 짝이없는, 모든 태그에 사용 가능한 global attribute도 있음

![image-20220203104537244](HTML.assets/image-20220203104537244.png)



탭의 순서를 

### 4. 시맨틱 태그 : 이름만 보고 감을 잡기 위해서

![image-20220203110423482](HTML.assets/image-20220203110423482.png)

시험!!! 객관식(너무 중요하고 개념문졔)

* 시맨틱태그를 사용하지않은 좌측, 시맨틱태그를 사용한 우측

![image-20220203111012647](HTML.assets/image-20220203111012647.png)

* SEO 검색엔진최적화!
  * div, span은 nonsemantic요소인데, 나머지 대부분은 시맨틱태그로 볼수있음

![image-20220203111142294](HTML.assets/image-20220203111142294.png)

![image-20220203111327447](HTML.assets/image-20220203111327447.png)

![image-20220203111342922](HTML.assets/image-20220203111342922.png)



![image-20220203111428123](HTML.assets/image-20220203111428123.png)

![image-20220203111809633](HTML.assets/image-20220203111809633.png)

* strong은 시멘틱한 요소
* b는 덜 시멘틱
* em은 시멘틱한 요소
* i는 덜 시멘틱
* span의 의미없는 : non시멘틱 (하나의 태그로 묶을 수 있다.)





### 그룹컨텐츠 태그

![image-20220203111903428](HTML.assets/image-20220203111903428.png)

* p : non 시멘틱, 하나의 문장안에 들어갈 수 있는 것. p안에 div 태그 못씀
* pre : 공백문자를 그대로 유지 (많이 안씀. html에 작성한 내용을 그대로 표현)

![image-20220203112334514](HTML.assets/image-20220203112334514.png)



* div : 블록 레벨 컨테이너
* 

### table : 시멘틱 태그

![image-20220203112518023](HTML.assets/image-20220203112518023.png)

![image-20220203112555375](HTML.assets/image-20220203112555375.png)

* 헷갈리는 것, 시험에 나옴 !!!!!!!!!!!!주의

![image-20220203112643057](HTML.assets/image-20220203112643057.png)

* colspan :  세로인것 두개를 합치니까 가로가 길어짐
* rowspan : 
* 다음에 들어갈 단어를 쓰세요...........!!!!!!!!!!!!!!!시험 100프로

![image-20220203112859479](HTML.assets/image-20220203112859479.png)

![image-20220203113553471](HTML.assets/image-20220203113553471.png)

눈에는똑같아도합쳐져있는게 보인다



### form에서 action, method가 중요하다.

* form은 사용자의 데이터를 입력받는 것

![image-20220203124233422](HTML.assets/image-20220203124233422.png)



### input : 속성 시험에 구체적으론 안나옴

![image-20220203124502547](HTML.assets/image-20220203124502547.png)

![image-20220203124719676](HTML.assets/image-20220203124719676.png)

* get방식 : 보안이 약함(보여도 되는 것들)
* type은 text로 되어있어서 문자열로 입력받겠다는 것임
* input의 name은 쿼리스트링의 key로 들어감(get방식)

![image-20220203124954648](HTML.assets/image-20220203124954648.png)

* post방식: boby에 담아서 보냄

![image-20220203125423375](HTML.assets/image-20220203125423375.png)



체크해야할것

![image-20220203130832880](HTML.assets/image-20220203130832880.png)



### input 유형

![image-20220203131155697](HTML.assets/image-20220203131155697.png)

* number : min , max, step 잘안씀

![image-20220203131301986](HTML.assets/image-20220203131301986.png)

![image-20220203131415890](HTML.assets/image-20220203131415890.png)

* color : 자주 안씀
* date 
* https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input



## 시험 문제 input 체크박스, 라디오 type, name 조심

![image-20220203132255442](HTML.assets/image-20220203132255442.png)

![image-20220203132132967](HTML.assets/image-20220203132132967.png)



### 학생설문 만들기

![image-20220203132315969](HTML.assets/image-20220203132315969.png)

![image-20220203132520171](HTML.assets/image-20220203132520171.png)

![image-20220203134844207](HTML.assets/image-20220203134844207.png)





# CSS

# CSS는 먼저 선택하고 스타일을 지정한다



![image-20220203140728331](HTML.assets/image-20220203140728331.png)

![image-20220203140754210](HTML.assets/image-20220203140754210.png)

![image-20220203141008962](HTML.assets/image-20220203141008962.png)



https://css-art.com/pure-css-lace/



# 프로젝트때 유용..

https://csslayout.io/

https://mybrandnewlogo.com/ko/color-gradient-generator





## 선택자

![image-20220203143558547](HTML.assets/image-20220203143558547.png)

![image-20220203143946074](HTML.assets/image-20220203143946074.png)

## 아이디선택자



css

#id_name{

​	

}

![image-20220203143908720](HTML.assets/image-20220203143908720.png)

html에서는 

<a id ="id_name">





## 속성 선택자

![image-20220203143821044](HTML.assets/image-20220203143821044.png)





## 자손결합자 : A B (A의 모든 자손중에서 B를 만족하는 것을 선택함)





## 자식결합자 : A > B

div > p {

  color: red;

}



## 일반 형제 결합자 A~B

![image-20220203145248753](HTML.assets/image-20220203145248753.png)

![image-20220203145004513](HTML.assets/image-20220203145004513.png)

## 인접 형제 결합자 A+B

A바로 옆에 있는 B를 충족하는 애만 선택 선택



* 아래 코드는 안됨!

![image-20220203145115564](HTML.assets/image-20220203145115564.png)

![image-20220203145138522](HTML.assets/image-20220203145138522.png)





## 의사 클래스 : 외우는게 아니라 그때그때 갖다쓰면됨..

![image-20220203145414184](HTML.assets/image-20220203145414184.png)

hover : 마우스가 올라가면..

```
### 1. 동적 의사 클래스
- **:link** : 사용자가 아직 한 번도 해당 링크를 누르지 않은 상태 ( a요소 기본 )
- **:visited** : 사용자가 한 번이라도 해당 링크를 누른 상태
- **:hover** : 사용자의 마우스 커서가 위에 올라가 있는 상태
- **:active** : 사용자의 마우스 커서가 클릭중인 상태
- **:focus** : tab키로 focus가 맞춰진 상태
### 2. 상태 의사 클래스
- **:checked** : input의 checkbox나 raidobutton이 체크된 상태
- **:enabled** : input의 "type=text", select, option에서 사용자가 선택한 상태
- **:disabled** : input의 "type=text", select, option을 사용자가 선택할 수 없도록 만든 상태출처 - [https://aboooks.tistory.com/311](https://aboooks.tistory.com/311)
### 3. 구조 의사 클래스
- **:first-child** : 모든 자식 요소 중에서 첫 번째에 위치하는 자식을 선택
- **:nth-child(n)** : 모든 자식 요소 중에서 n번째에 위치하는 자식을 선택
- **:last-child** : 모든 자식 요소 중에서 마지막에 위치하는 자식을 선택
- **:first-of-type** : 모든 자식 요소 중에서 첫 번째에 등장하는 특정 요소를 선택
- **:nth-of-type(n)** : 모든 자식 요소 중에서 n번째로 등장하는 특정 요소를 선택
- **:last-of-type** : 모든 자식 요소 중에서 마지막으로 등장하는 특정 요소를 선택
```



## 특정 :: 두개 (필요할 때 찾아쓰기)

![image-20220203145918951](HTML.assets/image-20220203145918951.png)

```
- **::first-letter** : 요소의 텍스트에서 첫 번째 글자에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::first-line** : 요소의 텍스트에서 첫 줄에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::before** : 요소의 콘텐츠 시작부분에 생성된 콘텐츠를 추가한다.
- **::after** : 요소의 콘텐츠 끝부분에 생성된 콘텐츠를 추가한다.
```

![image-20220203150053842](HTML.assets/image-20220203150053842.png)

![image-20220203150546960](HTML.assets/image-20220203150546960.png)

아이디 반드시 1개만!!



# 시험문제 이거 까지는 알기 (클래스까지는 알기>요소(h1)), 인라인은 거의 쓰지 말기![image-20220203150834897](HTML.assets/image-20220203150834897.png)

![image-20220203151015458](HTML.assets/image-20220203151015458.png)



## !important; - 최우선순위(그러나 쓰지말아라!)

![image-20220203151159510](HTML.assets/image-20220203151159510.png)



## 같은 우선순위가 있다면, 마지막에 정의된 것을 따름

![image-20220203153513784](HTML.assets/image-20220203153513784.png)



오랜지, 블루, 그린, 그린, 레드, 다크바이올렛, 옐로, 다크바이올렛



## 상속 컬러는 되고, border는 안되네?

텍스트는 물려받고, 박스는 물려받지 않는다.

![image-20220203154319995](HTML.assets/image-20220203154319995.png)



* 몰라도됨,, inherit 을 많이 쓰면 코드가 꼬임



![image-20220203154432916](HTML.assets/image-20220203154432916.png)





# 크기 단위 : 가변크기를 더 많이 씀 

시험은 rem, em 비교하기. 주의!



![image-20220203154851213](HTML.assets/image-20220203154851213.png)

![image-20220203155253626](HTML.assets/image-20220203155253626.png)

![image-20220203155434111](HTML.assets/image-20220203155434111.png)

![image-20220203155652023](HTML.assets/image-20220203155652023.png)

![image-20220203155934837](HTML.assets/image-20220203155934837.png)





## vw (font-size : vw)

![image-20220203160626519](HTML.assets/image-20220203160626519.png)

vmin: 최소크기, vmax : 최대크기 정할 수 있음

vmin 은 100분의 1 



![image-20220203160758717](HTML.assets/image-20220203160758717.png)

![image-20220203160539235](HTML.assets/image-20220203160539235.png)





## 색상 hsl는 거의안씀, a가 투명도

![image-20220203161243741](HTML.assets/image-20220203161243741.png)

## 필요할때마다 구글링

![image-20220203161401201](HTML.assets/image-20220203161401201.png)



## 

![image-20220203162909459](HTML.assets/image-20220203162909459.png)

![image-20220203163219895](HTML.assets/image-20220203163219895.png)

![image-20220203163514740](HTML.assets/image-20220203163514740.png)

![image-20220203163711945](HTML.assets/image-20220203163711945.png)



시험!!! 주의 margin, padding 다 똑같음



2개 : 십자가

3개 : 나누기

4개 : 시계방향



![image-20220203164132975](HTML.assets/image-20220203164132975.png)



border까지가 우리눈에 보이는 영역



### box 사이징은 어디까지를 기준으로 잡을 것인지를 보는 거구나, 어디까지가 100인지를 

![image-20220203165505831](HTML.assets/image-20220203165505831.png)

![image-20220203165749247](HTML.assets/image-20220203165749247.png)display는 text(텍스트)로 생각하자.....

display에서 알아야할 것은 블럭과 인라인이있다정도.



상하여백을 주고 싶다면 line-height로 지정.....( but 몰라도 됨)

![image-20220203170555256](HTML.assets/image-20220203170555256.png)

이런형태면 인라인 블럭 이겠구나!!!

![image-20220203170818579](HTML.assets/image-20220203170818579.png)

시험 ! display none은 공간조차 부여되지 않음.







* fixed : viewport를 기준으로 광고 붙어있는ㄱ ㅓ..!ㅁ

![image-20220203171342206](HTML.assets/image-20220203171342206.png)

![image-20220203172535041](HTML.assets/image-20220203172535041.png)

 



형에게 absolute를 주면 공중에 뜨고, 동생이 형자리에 가서 철썩 붙는다. (fixed도 붕뜬다.)

![image-20220203172618369](HTML.assets/image-20220203172618369.png)



형에게 relative를 주면 원래자리를 기준으로 하는것이 relative

![image-20220203172725123](HTML.assets/image-20220203172725123.png)

![image-20220203172958692](HTML.assets/image-20220203172958692.png)



총정리 :

![image-20220203174951821](HTML.assets/image-20220203174951821.png)

https://cantunsee.space/