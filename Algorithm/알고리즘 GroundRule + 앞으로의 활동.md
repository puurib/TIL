# 알고리즘 GroundRule + 앞으로의 활동

![image-20220209132918778](%ED%8C%8C%EC%9D%B4%EC%B0%B8%20%EC%84%A4%EC%B9%98.assets/image-20220209132918778.png)



### 파일 구조는 이렇게!

![image-20220209133911412](%ED%8C%8C%EC%9D%B4%EC%B0%B8%20%EC%84%A4%EC%B9%98.assets/image-20220209133911412.png)



## daily 과정





## 파일 

### sol.sh 생성

![image-20220209134836158](%ED%8C%8C%EC%9D%B4%EC%B0%B8%20%EC%84%A4%EC%B9%98.assets/image-20220209134836158.png)

1. cd ~ 로 이동 (홈 디렉토리로 이동)
2. code sol.sh (vscode로 sol.sh 파일을 생성)
3. 아래 코드를 넣고 저장하기

```
echo -e "import sys\\n\\nsys.stdin = open('input.txt')\n\nT = int(input())\n\n\nfor tc in range(1, T + 1):\n    \n    print(f'#{tc} ')\n" >> sol$1.py
```



### .bash_profile 생성

![image-20220209134928597](%ED%8C%8C%EC%9D%B4%EC%B0%B8%20%EC%84%A4%EC%B9%98.assets/image-20220209134928597.png)

![image-20220209134759580](%ED%8C%8C%EC%9D%B4%EC%B0%B8%20%EC%84%A4%EC%B9%98.assets/image-20220209134759580.png)

1. code Desktop/ (데스크탑으로 이동)

2. code . (현재 폴더에서 vscode 열기)
3. `.bash_profile` 파일 만들기
4. 아래 코드를 넣고 저장

```
alias sol='~/sol.sh'
```



### test

1. git bash 에서 `sol 파일명`

2. 파일이 생성되어 있는 것을 확인한다.