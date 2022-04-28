// 이동시키기 
const elem1 = document.querySelector('#list-1')
// 갤럭시버즈 선택
const targetElem = elem1.lastElementChild
// 맥북프로 선택 
const sourceElem = elem1.children[1]
// 갖다붙일곳.append(갖다붙일값)  
sourceElem.before(targetElem)

// [1] 노드 생성
const newNode = document.createElement('li')
// <li></li> 상태

// [2] 노드꾸미기
newNode.textContent = '전기모기채'
// <li>전기모기채</li> 상태
// [3] console 에 newNode 찍어보기

// [4] li를 갤럭시22 밑에 넣기
const elem2 = document.querySelector('#list-2').lastElementChild
elem2.append(newNode)

// 스타일우선순위가 높아져버려 좋지않고,
// 같은 걸 다른 요소에 적용할 때 불필요한 코드가 생김
// stylesheet에 적어놓고 id, clas를 변경하는 방식으로 사용하기
//elem1.style.backgroundColor = '#dd151d'
elem1.className = 'GreenBG'

// add, remove, toggle 형식 지원 (여러개 클래스)
// toggle - 있으면 제거 없으면 추가 
elem1.classList.add('WhiteFont')
elem1.classList.toggle('WhiteFont')
elem1.classList.toggle('WhiteFont')