<template>
  <div class="inputBox shadow">
    <!--v-model: input 과 데이터를 바인딩 -->
    <!--@keyup.enter 입력하고 엔터치면 addTodo()함수를 실행하라 -->
    <input type="text" v-model="newTodoItem" @keyup.enter="addTodo">
    <!--버튼을 입력할 때 마다 v-click-->
    <!-- <button @click="addTodo">add</button> -->
    <!--i 태그는 문자여서, span으로 감싸서 향후 스타일 처리 유용하게 함-->
    <span><i class="fa-solid fa-plus" @click="addTodo"></i></span>
    
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        newTodoItem: '',
      }
    },
    methods:{
      addTodo(){
        const todoObj = {
          item: this.newTodoItem, // 문자열
          completed: false,
        }

        if(this.newTodoItem){
        // localStorage.setItem(key, value) 이 객체가 문자열로 변환되어서 들어감
          localStorage.setItem(this.newTodoItem, JSON.stringify(todoObj))
          this.clearInput()
        }
      },
      // 인풋창을 깨끗하게
      clearInput(){
        this.newTodoItem = ''
      }
    },
  }
  
</script>

<style scoped>
  #input을 
  input:focus {
    outline: none;
  }
  input {
    border-style: none;
  }
  .shadow {
    box-shadow: 5px 10px 5px rgba(0, 0, 0, 0.03);
  }
  .inputBox {
    height: 50px;
    line-height: 50px;
    border-radius: 5px;
    background-color: white;
    border-style: none;
  }
</style>