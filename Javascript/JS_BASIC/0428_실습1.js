// 누르면 1증가 감소되게..
const minusBtn = document.querySelector('#minusBtn')
const plusBtn = document.querySelector('#plusBtn')
const number = document.querySelector('#number')


plusBtn.addEventListener('click', function() {
  console.log('plus');
  number.textContent += 1
})

minusBtn.addEventListener('click', function() {
  console.log('plus');
  number.textContent -= 1
})
