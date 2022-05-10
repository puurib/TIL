<template>
  <div>
    <input @keyup.enter="onInputKeyword" type="text" class="text-center w-75">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>
input {
  font-size: 1rem;
  border: 0;
  outline: 0;
  background: transparent;
  border-bottom: 3px solid rgb(161, 53, 228);
}
</style>