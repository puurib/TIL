# Git

## 1. Git이란?

* 분산 버전 관리 시스템 

* 코드의 히스토리(버전)을 관리하는 도구, 개발되어온 과정 파악 가능, 이전 버전과의 변경 사항 비교 및 분석

* git은 맨 나중 파일과, 변경 사항만을 저장한다.

* 백업, 복구, 협업

* 버전 : 컴퓨터 소프트웨어의 특정 상태
* 관리 : 어떤 일의 사무, 시설이나 물건의 유지, 개량
* 프로그램 : 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음



## 2. Git과 GitHub의 차이 

* Git은 분산 버전 관리 프로그램 그 자체를 의미, GitHub는 서버(=저장소) 역할



## 3. 서버(GitHub, GitLab 등)

* GitHub는 MS사의 서버를 사용
* GitLab은 서버를 내 컴퓨터 저장소에 구축할 수 있게 해준다. (보안 측면에서 용이)



## 4. Git에서 사용하는 README.md

* README.md는 프로젝트 설명서를 뜻한다.



## 5. CLI, GUI

* CLI (Command-Line Inperface) : 명령 줄 인터페이스
* GUI (Graphical User Interface) : 그래픽 기능을 사용하는 사용자 인터페이스



## 6. CMD, Power Shell, Git bash

* CMD : command의 준말, 윈도우 NT 계열(윈도우 2000/XP/2003/비스타 이상) 운영 체제의 명령 줄 해석기
* Power Shell : 마이크로소프트가 개발한 확장 가능한 명령 줄 인터페이스(CLI) 셸 및 스크립트 언어를 특징으로 하는 명령어 인터프리터이다.
* Git bash : Git 전용 프롬프트
  * Git bash에서 `code .`를 입력하면, 명령어를 입력한 위치에서 Visual Studio Code가 열린다.



## 7. Git에 사용되는 간단한 Linux 명령어

* `ls` : 현재 위치의 폴더, 파일 목록 보기
* `cd` : 현재 위치 이동하기
  * `cd ..` : 상위(부모) 폴더로 이동
  * `cd ~` :  user의 home으로 이동 (ex: C:\users\star3, C드라이브의 사용자 폴더를 의미한다.)
* `~` : user의 home
* `*` : 전체
* `mkdir 폴더이름` : 폴더 만들기
* `rmdir 폴더이름` = `rm -r 폴더이름` : 폴더삭제하기
* `-r` (recursive; 반복되는) : 디렉토리를 의미
* `-rf` : 강제적으로 지울 때 사용하는 명령어
* `touch 파일이름` : 파일 만들기 (Power Shell에서는 지원 안되는 명령어)
* `rm 파일이름` : 파일 지우기
* `tab` : 명령어 자동완성



## 8. Repository(저장소) = .git

* 특정 디렉토리를 버전 관리하는 저장소를 뜻함
* `git init`으로 저장소를 생성한다.
* `.git` : git을 이용해서 관리하는 모든 히스토리가 들어있는 폴더 = Repository
* `commit한다` : 
  * 특정 버전으로 남긴다. = Repository 안에 commit이 쌓여가는 것
  *  3가지 영역을 바탕으로 동작



## 9. Working Directory, Staging Area, Repositroy

* commit이 동작하는 3가지 영역을 뜻함



### 1) Working Directory

* 내가 작업하고 있는 실제 디렉토리
* 로컬에서 만든 디렉토리라면, git으로부터 추적되지 않는 상태이다.

* `git add` 로 추적 되지 않은 모든 파일, 추적 하고 있는 파일 중 수정 된 파일을 모두 Staging Area에 올린다.



### 2) Staging Area

* 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

* 이 때부터는 git으로부터 추적되는 상태이다.
* `git commit`으로 Repository로 넘어가게 된다.



### 3) Repository

* 커밋들이 저장되는 곳



## 8. Git 명령어

1. `git init` : 로컬 저장소 생성
2. `git --version` : git의 버전 확인
3. `git status` : git의 상태 보기
4. `git add` : git으로 버전 관리를 시작할 것이라고 알림
   * `git add .` : 현재 디렉토리의 모든 사항을 `git add`한다.
   * `git add 변경할 파일/폴더 이름` : 특정 파일/폴더만 `git add`한다.
5. `git commit` : commit이후 하나의 버전으로 남게 됨
   * `git commit -m "커밋 메세지"` : 커밋 메세지에 변경한 사항을 적고 commit을 진행한다.
6. `git push` : 
7. `git config --list` : 



* 주의 : `--global`은 모든 프로젝트, 저장소에 대해 적용되는 것, 교육에서는 프로젝트 별로 Github, GitLab을 사용할 예정이라 `--glabal`은 사용하지 않음

8. `git config (--global) user.name 유저이름` : 유저 이름 확인
9. `git config (--global) user.email 유저이메일` : 유저이메일 확인
10.  `git log` : git의 log를 봄
    * `git log commit아이디숫자4개 숫자4개` : commit아이디의 앞 숫자와, 뒷 숫자의 변동 사항을 보여줌

11. `git push` : commit된 내용을 remote 저장소로 push
12. `git clone git저장소주소` : remote 저장소의 내용을 복제 (이후 pull을 진행한다.)
13. `git pull` : remote 저장소의 내용을 pull

* 로컬에 있는 디렉토리와 git저장소를 연결하기(git 명령어 사용하는 위치 주의하기)

11. `git remote add origin git저장소주소`  : git저장소주소를 앞으로 origin이라고 부르겠다.
12. `git push -u origin master` : master를 origin으로 보내겠다.



## 9. Git-Repository 연결 

### 1) 로컬에 있는 디렉토리를 Git에 연결

① 로컬 디렉토리와 같은 이름의 Git 레포지토리를 생성한다.

② Git 레포지토리 주소를 복사한다.

③ 해당하는 로컬 디렉토리 내에서  `git remote add origin git저장소주소`  를 입력한다.

④ `git push -u origin master` 명령어로 master(`git init`한 디렉토리)를 origin으로 보낸다.



### 2) Git 레포지토리를 Clone해서 연결

① `git clone git저장소주소`로 저장소를 복사한다.

② `git pull`로 코드를 받아온다.



## 10. Public, Private

* public : 모두 공개, 누구나 가져갈 수 있음, 올릴 수는 없음

* private : 개인적인, 비공개