<template>
  <div class="d-flex justify-content-center w-100 h-75 mt-3">
    <ul>
      <li v-for="movie in myMovies" :key="movie.date">{{ movie.item }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    myMovies: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

  li {
    font-family: Cafe24Oneprettynight;
    display: flex;
    height: 30px;
  }

</style>
