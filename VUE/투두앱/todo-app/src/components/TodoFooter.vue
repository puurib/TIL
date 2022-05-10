<template>
  <div>
    <p>Todo Footer</p>
    <button @click="clearAll">clear</button>
  </div>
</template>

<script>
  export default {
    methods: {
      clearAll() {
        localStorage.clear()
      }
    }
  }
</script>

<style>
  p {
    color :rgb(0, 0, 0);
    font-family: Cafe24Oneprettynight;
  }
</style>