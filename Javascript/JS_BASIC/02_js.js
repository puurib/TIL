// for in - 순서보장 x 순회

const fruits = ['apple', 'banana']

for (const each in fruits) {
  console.log(each);
}

// for in 2
let myObj = {
  key1 : 1,
  key2 : 'test'
}


// for of - 순서보장 순회
const fruits1 = ['apple', 'banana']

for (each of fruits1) {
  console.log(each);
}

