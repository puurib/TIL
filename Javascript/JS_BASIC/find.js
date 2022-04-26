// 나이 40 이상 = 30 초과인 사람 찾기

const avengers= [
  {name: 'Tony Start', age:45},
  {name: 'Steve Rogers', age:32},
  {name: 'Thor', age:40}
]

const rlt = avengers.find((elem) => {
  return elem.age > 39
})

console.log(avengers)