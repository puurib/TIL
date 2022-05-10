<template>
  <div class="inputBox shadow">
    
    <input type="text" v-model="newMovieItem" @keyup.enter="onEnter">
    <button @click="onEnter" type="button" class="btn btn-outline-success btn-sm ml-3">+</button>
  </div>
</template>

<script>
  import EventBus from '../EventBus'

  export default {
    name: 'WatchListForm',
    data: () => {
      return {
        newMovieItem: '',
      }
    },
    methods:{
      onEnter(){
        if (this.newMovieItem) {
          const myMovie = {
            date: new Date().getTime(),
            item: this.newMovieItem,
          }
          EventBus.$emit('addMovie', myMovie)
          this.newMovieItem = ''
        }
      }
    },
  }
</script>

<style scoped>
  button {
    font-family: Cafe24Oneprettynight;
    line-height: auto;
    margin: 0 auto;
  }
  input:focus {
    outline: none;
  }
  input {
    border-style: none;
    height: 25px;
    font-family: Cafe24Oneprettynight;
  }
  .shadow {
    box-shadow: 1px 3px 1px rgba(0, 0, 0, 0.02);
  }
  .inputBox {
    height: 50px;
    line-height: 50px;
    border-radius: 5px;
    background-color: white;
    border-style: none;
  }

</style>