const elem1 = document.querySelector('#title-1')
console.log(elem1)

const elem2 = document.querySelector('#list-1')
console.log(elem2)

// li 태그 전체 선택시 -> li 태그만 넣기
const elemlist = document.querySelectorAll('li')
console.log(elemlist)

//

const myHtml = elem1.innerHTML

// += 되면 플러스, =는 다 없어질수도
elem2.innerHTML += '<li>에어팟프로</li>' 