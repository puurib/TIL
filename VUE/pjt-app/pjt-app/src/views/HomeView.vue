<template>
  <div class="home container">
    <div class="row d-flex justify-content-center">
      <movie-card 
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    ></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'HomeView',
  components: {
    MovieCard,
  },
  props: ['movieList'],
}

</script>
