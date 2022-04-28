const elem1 = document.querySelector('#list-1')

// 첫번째 방법
const firstElem = elem1.firstElementChild
console.log(firstElem)

// 두번째 방법
const children = elem1.children
console.log(children)

// 세번째 방법
const lastElem = elem1.lastElementChild
console.log(lastElem)
