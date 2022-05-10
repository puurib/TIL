<template>
  <div>
    <ul>
      <!-- v-for는 key를 줘라-->
      <li v-for="(todo, idx) in todos" :key="`todo-${idx}`">
        <span 
          :class="{completed:todo.completed}" 
          @click="toggleTodo(todo)">
          {{todo.item}}
        </span>
        <i 
          class="fa-solid fa-square-minus removeIcon" 
          @click="removeTodo(todo, idx)">
        </i>
      </li>
    </ul>
  </div>

</template>

<script>
  export default {
    data: function() {
      return {
        todos: [],
      }
    },
    methods: {
      removeTodo(todo, idx) {
        //console.log('click!')
        //localStorage.removeItem(key)
        localStorage.removeItem(todo)
        // splice 기존 배열을 변경 this.todos.splice(idx, 1)
        this.todos.splice(idx, 1)
      },
      toggleTodo(todo) {
        todo.completed = !todo.completed
        // 업데이트가 따로 없어서 지우고 쓰고를 다시 하는 것
        localStorage.removeItem(todo.item)
        localStorage.setItem(todo.item, JSON.stringify(todo))
      }
    },
    // 만들어 질 때 ~~ 하겠다라는 라이프사이클 훅 작성 - 만들자마다 콘솔에 created작성됨
    // 여기에 input에서 입력한 로컬스토리지의 키벨류를 넣음
    
    created() {
      if (localStorage.length > 0) {
        //console.log('created')
        for (var i = 0; i < localStorage.length; i++) {
          console.log(localStorage.key(i))
          // 문자열 가지고와서 객체형체로 parse
          const todoItem = localStorage.getItem(localStorage.key(i))
          this.todos.push(JSON.parse(todoItem))
        }
      }
    },
  }
</script>

<style scoped>
  li {
    display: flex;
    height: 30px;
    font-family: Cafe24Oneprettynight;
  }
  .removeIcon {
    color : rgb(255, 140, 140);
    margin-left: auto;
  }

  .completed {
    text-decoration: line-through;
    color : gray;
  }
</style>