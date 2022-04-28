// 이벤트 
const elem1 = document.querySelector('#content')
const elem2 = document.querySelector('#list-1')

// 
function myClick() {
  console.log('눌렀구나?');
}

elem1.addEventListener('click', myClick)


// 
function myClick(e) {
  console.log(e);
}

elem1.addEventListener('click', myClick)
elem2.addEventListener('click', myClick)